import fastapi
import pydantic

from unico_device_setuper.api import state, token

ROUTER = fastapi.APIRouter(prefix='/test', tags=['Test'])


class TestPayload(pydantic.BaseModel):
    ok: str


class TestResponse(pydantic.BaseModel):
    ok: str
    bucket_name: str
    username: str


# Create


@ROUTER.post('/create', response_model=TestResponse)
async def create_client_endpoint(payload: TestPayload, state: state.State, token: token.Token):
    return TestResponse(ok=payload.ok, bucket_name=state.oci.bucket_name, username=token.username)
