"""This module contains the Post schemas."""

from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    """Base class for Post model."""
    title: str
    body: str


class Post(PostBase):
    """Database post model."""
    id: int
    posted_at: datetime

    class Config:
        """Database configuration."""
        orm_mode = True


class PostCreate(PostBase):
    """Post creation model."""
