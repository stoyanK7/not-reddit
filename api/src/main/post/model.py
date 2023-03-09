"""This module contains the Post model."""

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.main.database import Base


class Post(Base):
    """Post model."""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
