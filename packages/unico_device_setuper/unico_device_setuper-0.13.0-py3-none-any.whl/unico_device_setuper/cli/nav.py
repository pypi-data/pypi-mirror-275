import asyncio
import contextlib
import datetime
import sys
import typing

import pydantic_core
import slugify

from unico_device_setuper.cli import stp
from unico_device_setuper.lib import cnsl, datadir, dl, sgic, unitech, utils

SETUPER_ACTIVITY_TIMEOUT = datetime.timedelta(seconds=10)


async def download_uninav_apk(setup: stp.Setup):
    change_log = await unitech.get_device_update_change_log.request(
        await setup.get_unitech_client()
    )
    assert change_log
    assert change_log.release_url
    assert change_log.latest_version_name
    uninav_download_url = pydantic_core.Url(change_log.release_url)
    uninav_install_path = datadir.get() / f'uninav{change_log.latest_version_name}.apk'
    if not uninav_install_path.exists():
        await dl.download_url(
            uninav_download_url, uninav_install_path, setup.http_client, uninav_install_path.name
        )
    return uninav_install_path


async def install_uninav(setup: stp.Setup):
    apk_path = await download_uninav_apk(setup)
    with contextlib.suppress(utils.SubprocessError):
        await setup.adb.uninstall('com.unico.dev.appmobile')
    await setup.adb.install(apk_path)


async def start_setuper_activity(setup: stp.Setup):
    await setup.adb.shell(
        'am start -n com.unico.dev.appmobile/.core.setuper.IdDeviceLoggerActivity'
    )


async def stop_uninav(setup: stp.Setup):
    await setup.adb.shell('am force-stop com.unico.dev.appmobile')


async def find_device_id_in_logs(logs: typing.AsyncIterable[str]):
    async for line in logs:
        line_parts = line.split('ID_DEVICE: ')
        if len(line_parts) > 1:
            return line_parts[-1]
    return None


async def get_id_device(setup: stp.Setup):
    await stop_uninav(setup)
    await setup.adb.logcat('-c')
    await start_setuper_activity(setup)
    try:
        return await asyncio.wait_for(
            find_device_id_in_logs(setup.adb.logcat_gen()),
            timeout=SETUPER_ACTIVITY_TIMEOUT.total_seconds(),
        )
    except TimeoutError:
        return None
    finally:
        await stop_uninav(setup)


async def get_next_name_increment(setup: stp.Setup):
    device_owner = input("Nom du propriétaire ('uni' par défaut): ") or 'uni'
    devices = await unitech.get_device_all_devices.request(await setup.get_unitech_client())
    if devices is None:
        cnsl.print_red('Impossible de récupérer la liste de devices')
        return None
    max_value = 0
    for device in devices:
        match slugify.slugify(device.name).split('-'):
            case ['tab', owner, 'sams', num] if owner == device_owner:
                with contextlib.suppress(ValueError):
                    max_value = max(int(num), max_value)
            case _:
                pass
    return f'tab.{device_owner}.sams.{max_value}'


async def register_device(setup: stp.Setup):
    device_id = await get_id_device(setup)
    if device_id is None:
        cnsl.print_red("Impossible de trouver l'id device")
        return
    cnsl.print_cyan(f'Id Device: {device_id}\n')

    device_name = await get_next_name_increment(setup)
    if device_name is None:
        cnsl.print_red('Impossible de trouver un nom')
        return
    cnsl.print_cyan(f'Name: {device_name}\n')

    register_response = await unitech.post_auth_device_register_device.request(
        await setup.get_unitech_client(), unitech.RegisterDevicePayload(device_name, device_id)
    )
    if isinstance(register_response, unitech.RegisterDeviceResponse):
        cnsl.print_greeen('Appareil enregistré')
    else:
        cnsl.print_red(f"Erreur lors de l'enregistrement de l'appareil: {register_response}")


def choose_product(products: list[sgic.GroupedOrderItem], name: str | None):
    if name is None:
        cnsl.print_blue('Choisir une licence:')
        product = cnsl.print_choose(
            products, prompt='Licences ', formater=lambda c: c.product_name.strip()
        )
        cnsl.print()
        return product

    slugified_name = slugify.slugify(name)
    product = next((p for p in products if slugify.slugify(p.product_name) == slugified_name), None)
    if product is None:
        cnsl.print_red(f'Aucun client avec le nom [hot_pink3]`{name}`[/hot_pink3]')
        sys.exit()

    return product


async def list_products(setup: stp.Setup):
    sygic_client = await setup.get_sygic_client()
    products = await sygic_client.get_products()
    cnsl.print_blue(f'{products}')
    return products


async def register_sygic_license(setup: stp.Setup):
    sygic_client = await setup.get_sygic_client()
    products = await list_products(setup)
    product = choose_product(products, name=None)

    device_id = await get_id_device(setup)
    if device_id is None:
        cnsl.print_red("Impossible de trouver l'id device")
        return

    device_name = next(
        (
            d.name
            for d in await unitech.get_device_all_devices.request(await setup.get_unitech_client())
            or []
            if d.id_device == device_id
        ),
        None,
    )
    if device_name is None:
        cnsl.print_red("Impossible de trouver le nom de l'appereil")
        return

    await sygic_client.register_licence(
        product_id=product.product_id,
        purchase_period=product.purchase_period,
        device_id=device_id,
        device_name=device_name,
    )
