import dataclasses
import enum
import typing

import httpx
import pydantic_core

from unico_device_setuper.lib import aapt, adb, auth, cnsl, datadir, sgic, unitech


class Env(enum.Enum):
    DEV = 'dev'
    PRE_PROD = 'pre-prod'
    PROD = 'prod'
    LOCAL = 'local'

    @staticmethod
    def get_default():
        if datadir.is_release_version():
            return Env.PROD
        return Env.LOCAL


@dataclasses.dataclass
class Args:
    restart_adb: bool
    unitech_client: str | None
    env: Env


def get_unitech_api_base_url(args: Args):
    if args.env == Env.LOCAL:
        return pydantic_core.Url('http://localhost:3000')
    return pydantic_core.Url(f'https://api.{(args.env).value}.unicofrance.com')


@dataclasses.dataclass
class Setup:
    args: Args
    _unitech_client: unitech.Client
    _sygic_client: sgic.Client | None
    http_client: httpx.AsyncClient
    adb: adb.Adb
    aapt: aapt.Aapt

    @staticmethod
    async def execute_for_each_device(
        args: Args, handler: typing.Callable[['Setup'], typing.Awaitable[None]]
    ):
        cnsl.print_gray(f'Environement: {args.env.value}')
        async with (
            unitech.Client(base_url=str(get_unitech_api_base_url(args))) as unitech_client,
            httpx.AsyncClient() as http_client,
            adb.Adb.make(http_client, restart_server=args.restart_adb) as adb_,
        ):
            async for _ in adb_.for_each_device():
                async with aapt.Aapt.make(adb_, http_client) as aapt_:
                    await handler(
                        Setup(
                            args=args,
                            _unitech_client=unitech_client,
                            _sygic_client=None,
                            http_client=http_client,
                            adb=adb_,
                            aapt=aapt_,
                        )
                    )

    async def get_unitech_client(self):
        headers = self._unitech_client.get_async_httpx_client().headers
        auth_header_name = 'Authorization'
        if headers.get(auth_header_name) is None:
            headers[auth_header_name] = 'Bearer ' + await auth.get_unitech_auth_token(
                get_unitech_api_base_url(self.args), client_name=self.args.unitech_client
            )
        return self._unitech_client

    async def get_sygic_client(self):
        if self._sygic_client is None:
            self._sygic_client = await sgic.Client.make(self.http_client)
        return self._sygic_client
