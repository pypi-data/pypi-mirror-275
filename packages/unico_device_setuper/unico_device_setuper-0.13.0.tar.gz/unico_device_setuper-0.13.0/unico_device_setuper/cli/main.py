import asyncio
import enum
import sys
import typing

import rich
import typer

import unico_device_setuper
from unico_device_setuper.cli import nav, pkg, stp
from unico_device_setuper.lib import auth, datadir

APP = typer.Typer(pretty_exceptions_enable=False)


@APP.callback(invoke_without_command=True)
def main(ctx: typer.Context, *, version: bool = False, data_dir: bool = False):
    if version:
        rich.print(unico_device_setuper.__version__)
        sys.exit(0)

    if data_dir:
        rich.print(datadir.get())
        sys.exit(0)

    if len(sys.argv) == 1:
        typer.echo(ctx.get_help())


@APP.command()
def logout(platform: auth.LoginPlatform):
    auth.clear_credentials(platform)


class PackageAction(enum.Enum):
    LIST = 'list'
    UNINSTALL = 'uninstall'


async def _package(action: PackageAction, args: stp.Args):
    match action:
        case PackageAction.LIST:
            handler = pkg.list_packages
        case PackageAction.UNINSTALL:
            handler = pkg.uninstall_packages

    await stp.Setup.execute_for_each_device(args, handler)


@APP.command()
def package(
    action: PackageAction,
    *,
    restart_adb: bool = False,
    unitech_client: typing.Optional[str] = None,  # noqa: UP007
    env: typing.Optional[stp.Env] = None,  # noqa: UP007
):
    asyncio.run(
        _package(
            action,
            stp.Args(
                restart_adb=restart_adb,
                unitech_client=unitech_client,
                env=env or stp.Env.get_default(),
            ),
        )
    )


class UninavAction(enum.Enum):
    INSTALL = 'install'
    REGISTER = 'register'


async def _uninav(action: UninavAction, args: stp.Args):
    match action:
        case UninavAction.INSTALL:
            handler = nav.install_uninav
        case UninavAction.REGISTER:
            handler = nav.register_device

    await stp.Setup.execute_for_each_device(args, handler)


@APP.command()
def uninav(
    action: UninavAction,
    *,
    restart_adb: bool = False,
    unitech_client: typing.Optional[str] = None,  # noqa: UP007
    env: typing.Optional[stp.Env] = None,  # noqa: UP007
):
    asyncio.run(
        _uninav(
            action,
            stp.Args(
                restart_adb=restart_adb,
                unitech_client=unitech_client,
                env=env or stp.Env.get_default(),
            ),
        )
    )


class SygicAction(enum.Enum):
    REGISTER = 'register'


async def _sygic(action: SygicAction, args: stp.Args):
    match action:
        case SygicAction.REGISTER:
            handler = nav.register_sygic_license

    await stp.Setup.execute_for_each_device(args, handler)


@APP.command()
def sygic(
    action: SygicAction,
    *,
    restart_adb: bool = False,
    unitech_client: typing.Optional[str] = None,  # noqa: UP007
    env: typing.Optional[stp.Env] = None,  # noqa: UP007
):
    asyncio.run(
        _sygic(
            action,
            stp.Args(
                restart_adb=restart_adb,
                unitech_client=unitech_client,
                env=env or stp.Env.get_default(),
            ),
        )
    )
