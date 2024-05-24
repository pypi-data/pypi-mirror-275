import contextlib
import dataclasses
import typing

import fastapi
import fastapi.openapi.docs
import starlette.middleware
import starlette.middleware.base

import unico_device_setuper
from unico_device_setuper.api import routes, state, token_verifier
from unico_device_setuper.lib import cfg, oci

type StateMaker = typing.Callable[[fastapi.FastAPI], typing.AsyncContextManager[state.State]]
type Middleware = typing.Callable[
    [fastapi.Request, typing.Callable[[fastapi.Request], typing.Awaitable[fastapi.Response]]],
    typing.Awaitable[fastapi.Response],
]


class HasRouter(typing.Protocol):
    ROUTER: fastapi.APIRouter


@dataclasses.dataclass
class ApiInfo:
    title: str
    contact_name: str
    contact_url: str
    contact_email: str


@contextlib.asynccontextmanager
async def make_state(config: cfg.Config, app: fastapi.FastAPI):
    app.version = unico_device_setuper.__version__

    async with oci.Context.make(config.oci) as oci_:
        yield state.RawState(
            config=config, token_verifier=token_verifier.TokenVerifier(config.security), oci=oci_
        )


def make_app_from_config(config: cfg.Config):
    return make_app(
        ApiInfo(
            title='Device Setuper',
            contact_name='Unico France',
            contact_url='https://www.unicofrance.com/',
            contact_email='contact@unicofrance.com',
        ),
        routes=routes.ROUTES,
        state_maker=lambda app: make_state(config=config, app=app),
        middlewares=[],
    )


def make_app(
    api_info: ApiInfo,
    *,
    routes: typing.Sequence[HasRouter],
    state_maker: StateMaker,
    middlewares: list[Middleware],
):
    @contextlib.asynccontextmanager
    async def lifespan(app: fastapi.FastAPI):
        async with state_maker(app) as state:
            yield state.attach()

    app = fastapi.FastAPI(
        lifespan=lifespan,
        title=api_info.title,
        contact={
            'name': api_info.contact_name,
            'url': api_info.contact_url,
            'email': api_info.contact_email,
        },
        middleware=[
            starlette.middleware.Middleware(
                starlette.middleware.base.BaseHTTPMiddleware, dispatch=middleware
            )
            for middleware in middlewares
        ],
    )

    for route in routes:
        app.include_router(route.ROUTER)

    return app
