from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.user.rabbitmq import connect_to_rabbitmq, disconnect_from_rabbitmq


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan[AppType]:
    connect_to_rabbitmq()
    yield
    disconnect_from_rabbitmq()
