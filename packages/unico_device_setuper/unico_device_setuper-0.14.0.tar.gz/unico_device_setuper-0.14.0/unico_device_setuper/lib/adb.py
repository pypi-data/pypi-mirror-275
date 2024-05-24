import contextlib
import dataclasses
import enum
import pathlib

import httpx
import pydantic_core
import slugify

from unico_device_setuper.lib import cnsl, datadir, dl, utils

ADB_DOWNLOAD_URL = pydantic_core.Url(
    'https://dl.google.com/android/repository/platform-tools-latest-darwin.zip'
)


class DeviceStatus(enum.Enum):
    DEVICE = enum.auto()
    UNAUTHORIZED = enum.auto()
    OFFLINE = enum.auto()
    NO_DEVICE = enum.auto()
    NO_STATUS = enum.auto()
    UNKNOWN_STATUS = enum.auto()

    def format_error(self):
        match self:
            case DeviceStatus.DEVICE:
                return None
            case DeviceStatus.UNAUTHORIZED:
                return 'Non autorisé'
            case DeviceStatus.OFFLINE:
                return 'Inatteignable'
            case DeviceStatus.NO_DEVICE:
                return 'Non connecté'
            case DeviceStatus.NO_STATUS:
                return 'Aucun status'
            case DeviceStatus.UNKNOWN_STATUS:
                return 'Status inconnu'

    @staticmethod
    def parse(value: str | None):
        if value is None:
            return DeviceStatus.NO_STATUS

        for status in DeviceStatus:
            if slugify.slugify(status.name) == slugify.slugify(value):
                return status

        cnsl.warn(f"Status de l'appareil inconnu : {value}")
        return DeviceStatus.UNKNOWN_STATUS


@dataclasses.dataclass
class DeviceInfos:
    product: str | None = None
    model: str | None = None

    def format(self):
        infos: list[str] = []
        if self.product is not None:
            infos.append(f'produit: {self.product}')
        if self.model is not None:
            infos.append(f'modèle: {self.model}')
        return ', '.join(infos)

    @staticmethod
    def parse(values: list[str]):
        infos = DeviceInfos()
        for value in values:
            name, _, info = value.partition(':')
            for field in dataclasses.fields(DeviceInfos):
                if field.name == name and issubclass(str, field.type):
                    setattr(infos, field.name, info)
        return infos


@dataclasses.dataclass
class Device:
    serial: str
    status: DeviceStatus
    infos: DeviceInfos

    @property
    def label(self):
        return f'{self.serial}{f' ({infos})' if (infos := self.infos.format()) else ''}'

    @staticmethod
    def parse(line: str):
        match line.split():
            case [serial, status_value, *infos_values]:
                pass
            case [serial]:
                status_value = None
                infos_values = []
            case _:
                return None

        return Device(
            serial=serial,
            status=DeviceStatus.parse(status_value),
            infos=DeviceInfos.parse(infos_values),
        )

    @staticmethod
    async def parse_all(adb: 'Adb'):
        reached_device_list = False
        for line in await adb.devices('-l'):
            if line.strip() == 'List of devices attached':
                reached_device_list = True
                continue

            if not reached_device_list:
                continue
            if (device := Device.parse(line)) is not None:
                yield device


@dataclasses.dataclass
class Adb:
    adb_exe: pathlib.Path
    device: Device | None

    @contextlib.asynccontextmanager
    @staticmethod
    async def make(http_client: httpx.AsyncClient, *, restart_server: bool):
        adb_path = datadir.get() / 'adb'

        if not utils.is_executable(adb_path):
            await dl.download_and_extract_zipped_executable(
                ADB_DOWNLOAD_URL, pathlib.Path('adb'), adb_path, http_client
            )

        ctx = Adb(adb_path, device=None)
        if restart_server:
            await ctx.kill_server()
        await ctx.start_server()
        yield ctx

    async def for_each_device(self):
        any_device = False
        async for device in Device.parse_all(self):
            any_device = True

            status_error = device.status.format_error()
            if status_error is not None:
                cnsl.warn(f'Appareil ignoré {device.label}: {status_error}')
                continue

            self.device = device
            cnsl.print_gray(f'Appareil: {device.label}\n')
            yield

        if not any_device:
            cnsl.warn('Aucun appreil trouvé')

    def _exec_gen(self, *args: object):
        return utils.exec_proc(self.adb_exe, *map(str, args))

    async def _exec(self, *args: object):
        return [line async for line in utils.exec_proc(self.adb_exe, *map(str, args))]

    #

    def devices(self, *args: str):
        return self._exec('devices', *args)

    #

    def start_server(self):
        return self._exec('start-server')

    def kill_server(self):
        return self._exec('kill-server')

    #

    def logcat(self, *args: str):
        return self._exec('logcat', *args)

    def logcat_gen(self, *args: str):
        return self._exec_gen('logcat', *args)

    #

    def install(self, local_apk_path: pathlib.Path):
        return self._exec('install', local_apk_path)

    def uninstall(self, package_name: str):
        return self._exec('uninstall', package_name)

    #

    def shell_gen(self, cmd: str):
        return self._exec_gen('shell', cmd)

    def shell(self, cmd: str):
        return self._exec('shell', cmd)

    #

    async def push(self, local_path: pathlib.Path, remote_path: pathlib.Path):
        return await self._exec('push', local_path, remote_path)
