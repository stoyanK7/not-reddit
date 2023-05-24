import asyncio
from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.shared.database.main import engine
from src.main.vote.service import VoteService
from src.main.vote.model import Base


@asynccontextmanager
async def lifespan(app: VoteService) -> Lifespan[AppType]:
    create_database_tables()
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.user_registered_amqp_consumer.consume(loop))
    await task
    task = loop.create_task(app.post_created_amqp_consumer.consume(loop))
    await task
    task = loop.create_task(app.comment_created_amqp_consumer.consume(loop))
    await task
    task = loop.create_task(app.post_vote_casted_amqp_publisher.prepare_connection(loop))
    await task
    task = loop.create_task(app.comment_vote_casted_amqp_publisher.prepare_connection(loop))
    await task
    task = loop.create_task(app.user_deleted_amqp_consumer.consume(loop))
    await task
    yield


def create_database_tables():
    Base.metadata.create_all(bind=engine)
