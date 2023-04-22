from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.user.rabbitmq import rabbitmq_connection


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan[AppType]:
    """Close RabbitMQ connection after app shutdown."""
    yield
    rabbitmq_connection.close()
