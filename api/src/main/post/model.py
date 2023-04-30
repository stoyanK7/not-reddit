import enum

from sqlalchemy import Column, String, Integer, DateTime, Enum
from sqlalchemy.sql import func

from src.main.shared.database.main import Base


class PostType(enum.Enum):
    text = 1


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    username = Column(String)
    type = Column(Enum(PostType))
    votes = Column(Integer, server_default="0")


class User(Base):
    __tablename__ = "users_oid"

    oid = Column(String, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True, index=True)
