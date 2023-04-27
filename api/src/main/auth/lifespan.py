from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.auth.service import AuthService
from src.main.auth.util import load_openid_config


@asynccontextmanager
async def lifespan(app: AuthService) -> Lifespan[AppType]:
    await load_openid_config()
    yield
