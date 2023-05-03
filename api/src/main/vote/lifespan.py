from contextlib import asynccontextmanager

from fastapi.applications import AppType
from starlette.types import Lifespan

from src.main.shared.database.main import engine
from src.main.vote.service import VoteService
from src.main.vote.model import Base


@asynccontextmanager
async def lifespan(app: VoteService) -> Lifespan[AppType]:
    create_database_tables()
    yield


def create_database_tables():
    Base.metadata.create_all(bind=engine)
