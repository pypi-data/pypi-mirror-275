import contextlib
import dataclasses
import datetime
import functools
import pathlib
import typing

import oci_client

from unico_device_setuper.lib import cfg, utils

FILE_URL_PREFIX = 'file://'


@dataclasses.dataclass
class CreatedObject:
    path: pathlib.Path
    creation_datetime: datetime.datetime


class ResponseLike(typing.Protocol):
    @property
    def status_code(self) -> int: ...

    @functools.cached_property
    def text(self) -> str: ...


def _check_response(action: str, response: ResponseLike, accepted_status: set[int] | None = None):
    if accepted_status is None:
        accepted_status = {200}

    if response.status_code not in accepted_status:
        raise RuntimeError(f'{response.status_code} Could not {action}: {response.text}')


async def _get_namespace(client: oci_client.Client):
    namespace_response = await client.objectstorage_get('/n')
    _check_response('get namespace', namespace_response)
    assert isinstance(namespace_response.json, str)
    return namespace_response.json


async def _create_bucket(client: oci_client.Client, name: str, namespace: str):
    list_response = await client.objectstorage_get(
        f'/n/{namespace}/b/?compartmentId={client.tenant_id}'
    )
    _check_response('list existing buckets', list_response)

    assert isinstance(list_response.json, list)
    for bucket in list_response.json:
        assert isinstance(bucket, dict)
        if bucket['name'] == name:
            return

    # do not check create response
    # if it fails putting objects in it will fail too
    # this allows to not crash on race conditions

    await client.objectstorage_post(
        f'/n/{namespace}/b/', {'compartmentId': client.tenant_id, 'name': name}
    )


def file_part_generator(file: pathlib.Path, part_size_bytes: int):
    with file.open('rb') as f:
        while len(content := f.read(part_size_bytes)) > 0:
            yield content


@dataclasses.dataclass
class _MultipartUpload:
    id: str
    name: str
    part_num_ref_map: dict[int, str] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class Context:
    bucket_name: str
    namespace: str
    client: oci_client.Client
    upload_part_size: int
    config: cfg.Oci

    @contextlib.asynccontextmanager
    @staticmethod
    async def make(config: cfg.Oci):
        async with oci_client.Client.from_config(config.client) as client:
            namespace = await _get_namespace(client)
            await _create_bucket(client, config.bucket_name, namespace)

            yield Context(
                bucket_name=config.bucket_name,
                namespace=namespace,
                client=client,
                upload_part_size=config.upload_part_size,
                config=config,
            )

    async def delete(self, object_path: pathlib.Path):
        print(f'deleting {object_path}')  # noqa: T201
        delete_response = await self.client.objectstorage_delete(
            f'/n/{self.namespace}/b/{self.bucket_name}/o/{object_path}'
        )
        _check_response('delete object', delete_response, accepted_status={204, 404})

    async def _create_multipart_upload(self, object_path: pathlib.Path):
        print(f'creating {object_path}')  # noqa: T201
        upload_name = str(object_path)
        upload_create_response = await self.client.objectstorage_post(
            f'/n/{self.namespace}/b/{self.bucket_name}/u', {'object': upload_name}
        )
        _check_response('create new upload', upload_create_response)

        assert isinstance(upload_create_response.json, dict)
        upload_id = upload_create_response.json['uploadId']
        assert isinstance(upload_id, str)
        return _MultipartUpload(id=upload_id, name=upload_name)

    async def _upload_part(self, num: int, content: bytes, upload: _MultipartUpload):
        num += 1
        upload_part_response = await self.client.objectstorage_put(
            f'/n/{self.namespace}/b/{self.bucket_name}/u/{upload.name}'
            f'?uploadId={upload.id}&uploadPartNum={num}',
            content,
        )
        _check_response('upload part', upload_part_response)
        upload.part_num_ref_map[num] = upload_part_response.headers['Etag']

    async def _commit_upload(self, upload: _MultipartUpload):
        commit_upload_response = await self.client.objectstorage_post(
            f'/n/{self.namespace}/b/{self.bucket_name}/u/{upload.name}?uploadId={upload.id}',
            {
                'partsToCommit': [
                    {'etag': ref, 'partNum': num} for num, ref in upload.part_num_ref_map.items()
                ]
            },
        )
        _check_response('commit uplaod', commit_upload_response)

    async def _abbort_upload(self, upload: _MultipartUpload):
        abbort_upload_response = await self.client.objectstorage_delete(
            f'/n/{self.namespace}/b/{self.bucket_name}/u/{upload.name}?uploadId={upload.id}'
        )
        _check_response('abort upload', abbort_upload_response)

    async def upload_file(self, object_path: pathlib.Path, file_path: pathlib.Path):
        upload = await self._create_multipart_upload(object_path)
        try:
            for num, content in enumerate(file_part_generator(file_path, self.upload_part_size)):
                await self._upload_part(num, content, upload)
            await self._commit_upload(upload)
        except:
            await self._abbort_upload(upload)
            raise

    async def upload_object(self, object_path: pathlib.Path, data: bytes):
        print(f'creating {object_path}')  # noqa: T201
        url = f'/n/{self.namespace}/b/{self.bucket_name}/o/{object_path}'
        upload_create_response = await self.client.objectstorage_put(url, data)
        _check_response('create new object', upload_create_response)

    async def list_(self, prefix: pathlib.Path):
        list_object_response = await self.client.objectstorage_get(
            f'/n/{self.namespace}/b/{self.bucket_name}/o?prefix={prefix}&fields=name,timeCreated'
        )
        _check_response('list objects', list_object_response)

        assert isinstance(list_object_response.json, dict)
        objects = list_object_response.json['objects']
        assert isinstance(objects, list)
        for object in objects:
            assert isinstance(object, dict)
            name = object['name']
            assert isinstance(name, str)
            creation_datetime = object['timeCreated']
            assert isinstance(creation_datetime, str)
            yield CreatedObject(
                pathlib.Path(name), datetime.datetime.fromisoformat(creation_datetime)
            )

    async def get_file(self, object_path: pathlib.Path, file_path: pathlib.Path):
        with file_path.open('wb') as file:
            get_object_response = await self.client.objectstorage_get(
                f'/n/{self.namespace}/b/{self.bucket_name}/o/{object_path}', file
            )

        if get_object_response.status_code != 200:
            get_object_response.content = file_path.read_bytes()
            file_path.unlink(missing_ok=True)
            _check_response('get file', get_object_response)

    async def get_object(self, path: pathlib.Path):
        get_object_response = await self.client.objectstorage_get(
            f'/n/{self.namespace}/b/{self.bucket_name}/o/{path}'
        )
        _check_response('get object', get_object_response)
        return get_object_response.content

    async def exists(self, path: pathlib.Path):
        response = await self.client.objectstorage_head(
            f'/n/{self.namespace}/b/{self.bucket_name}/o/{path}'
        )
        _check_response('checking object', response, {200, 404})
        return response.status_code == 200

    async def pre_authenticate(self, name: str, duration: datetime.timedelta, path: pathlib.Path):
        response = await self.client.objectstorage_post(
            f'/n/{self.namespace}/b/{self.bucket_name}/p',
            {
                'accessType': 'ObjectRead',
                'name': name,
                'objectName': str(path),
                'timeExpires': (utils.now() + duration)
                .astimezone(datetime.UTC)
                .strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            },
        )
        _check_response('create pre-authenticated request', response)
        assert isinstance(response.json, dict)
        url = response.json['fullPath']
        assert isinstance(url, str)
        return url
