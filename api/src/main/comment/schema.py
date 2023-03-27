"""This module contains the Comment schemas."""

from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    """Base class for Comment model."""
    body: str
    user_id: int
    post_id: int


class Comment(CommentBase):
    """Database comment model."""
    id: int
    commented_at: datetime

    class Config:
        """Database configuration."""
        orm_mode = True


class CommentCreate(CommentBase):
    """Comment creation model."""
