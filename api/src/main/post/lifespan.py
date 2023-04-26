import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.post.rabbitmq import consume_messages


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan[AppType]:
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(consume_messages(loop))
    yield
