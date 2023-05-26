import asyncio
from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.shared.database.main import Base, engine
from src.main.award.service import AwardService


@asynccontextmanager
async def lifespan(app: AwardService) -> Lifespan[AppType]:
    create_database_tables()
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.post_awarded_amqp_publisher.prepare_connection(loop))
    await task
    task = loop.create_task(app.comment_awarded_amqp_publisher.prepare_connection(loop))
    await task
    yield


def create_database_tables():
    Base.metadata.create_all(bind=engine)
