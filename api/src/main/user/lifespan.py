import asyncio
from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.shared.database.main import engine, Base
from src.main.user.service import UserService


@asynccontextmanager
async def lifespan(app: UserService) -> Lifespan[AppType]:
    create_database_tables()
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.user_registration_amqp_publisher.prepare_connection(loop))
    await task
    yield


def create_database_tables():
    Base.metadata.create_all(bind=engine)
