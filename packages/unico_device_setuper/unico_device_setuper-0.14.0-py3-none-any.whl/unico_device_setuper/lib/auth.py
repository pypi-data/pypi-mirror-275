import contextlib
import enum
import getpass
import json
import sys
import typing

import httpx
import keyring
import keyring.errors
import pydantic
import slugify

from unico_device_setuper.lib import cnsl, unitech, utils


class LoginPlatform(enum.Enum):
    UNITECH = 'unitech'
    SYGIC = 'sygic'

    @property
    def keyring_credentials_key(self):
        return f'{self.name}_credentials'


class UnitechCredentials(pydantic.BaseModel):
    username: str
    password: str


class SygicCredential(pydantic.BaseModel):
    api_key: str


KEYRING_CREDENTIALS_KEY = 'unitech_credentials'


async def get_credentials[T: pydantic.BaseModel](
    login_platform: LoginPlatform,
    callback: typing.Callable[[str, str], typing.Awaitable[T]],
    credential_type: type[T],
) -> T:
    encoded_credentials = keyring.get_password(
        utils.APP_NAME, login_platform.keyring_credentials_key
    )
    if encoded_credentials is not None:
        with contextlib.suppress(pydantic.ValidationError):
            return credential_type.model_validate_json(encoded_credentials)

    cnsl.print_blue(f'Connexion à votre compte {login_platform.name.capitalize()}:')
    username = input("Nom d'utilisateur: ")
    password = getpass.getpass('Mot de passe: ')
    cnsl.print('')

    credentials = await callback(username, password)

    keyring.set_password(
        utils.APP_NAME, login_platform.keyring_credentials_key, credentials.model_dump_json()
    )
    return credentials


def clear_credentials(login_platform: LoginPlatform):
    with contextlib.suppress(keyring.errors.PasswordDeleteError):
        keyring.delete_password(utils.APP_NAME, login_platform.keyring_credentials_key)


def choose_client(clients: list[unitech.LoginChooseResponseClientsItem], name: str | None):
    if name is None:
        cnsl.print_blue('Chosir un client:')
        client = cnsl.print_choose(clients, prompt='Client: ', formater=lambda c: c.name.strip())
        cnsl.print()
        return client

    slugified_name = slugify.slugify(name)
    client = next((c for c in clients if slugify.slugify(c.name) == slugified_name), None)
    if client is None:
        cnsl.print_red(f'Aucun client avec le nom [hot_pink3]`{name}`[/hot_pink3]')
        sys.exit()

    return client


async def get_unitech_auth_token(unitech_api_base_url: pydantic.HttpUrl, client_name: str | None):
    credentials = await get_credentials(
        LoginPlatform.UNITECH,
        lambda username, password: utils.wrap_async(
            UnitechCredentials(username=username, password=password)
        ),
        credential_type=UnitechCredentials,
    )
    api_client = unitech.Client(base_url=str(unitech_api_base_url))
    login_first_stage_response = await unitech.post_auth_login.detailed_request(
        client=api_client, body=unitech.LoginPayload(credentials.username, credentials.password)
    )
    if login_first_stage_response.status_code != 200:
        clear_credentials(LoginPlatform.UNITECH)
        error_message = 'Erreur inconnue'
        with contextlib.suppress(json.JSONDecodeError, KeyError):
            error_message = json.loads(login_first_stage_response.content)['displayMessage']
        cnsl.print_red(f'{error_message}')
        sys.exit()

    assert isinstance(login_first_stage_response.parsed, unitech.LoginChooseResponse)

    client = choose_client(login_first_stage_response.parsed.clients, name=client_name)
    login_second_stage_response = await unitech.post_auth_login.request(
        client=api_client,
        body=unitech.LoginPayload(credentials.username, credentials.password, id_client=client.id),
    )
    assert isinstance(login_second_stage_response, unitech.LoginTokenResponse)
    return login_second_stage_response.access_token


async def sygic_login(http_client: httpx.AsyncClient, username: str, password: str):
    response = await http_client.post(
        url='https://api.bls.sygic.com/api/v1/authentication',
        json={'userEmail': username, 'password': password},
    )
    return SygicCredential(api_key=response.json().get('apiKey'))


async def get_sygic_api_key(http_client: httpx.AsyncClient):
    return (
        await get_credentials(
            LoginPlatform.SYGIC,
            lambda username, password: sygic_login(http_client, username, password),
            credential_type=SygicCredential,
        )
    ).api_key
