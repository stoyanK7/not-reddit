import asyncio
from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.shared.database.main import engine
from src.main.post.service import PostService
from src.main.post.model import Base


@asynccontextmanager
async def lifespan(app: PostService) -> Lifespan[AppType]:
    create_database_tables()
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.successful_registration_amqp_consumer.consume(loop))
    await task
    task = loop.create_task(app.post_creation_amqp_publisher.prepare_connection(loop))
    await task
    yield


def create_database_tables():
    Base.metadata.create_all(bind=engine)
