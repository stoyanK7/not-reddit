"""This module contains the Comment model."""

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.main.database import Base


class Comment(Base):
    """Comment model."""

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    user_id = Column(Integer)
    post_id = Column(Integer)
    commented_at = Column(DateTime(timezone=True), server_default=func.now())
