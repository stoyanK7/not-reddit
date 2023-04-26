from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.user.rabbitmq import channel, rabbitmq_connection


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan[AppType]:
    yield
    channel.close()
    rabbitmq_connection.close()
