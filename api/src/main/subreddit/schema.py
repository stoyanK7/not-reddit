"""This module contains the Subreddit schemas."""

from datetime import datetime
from pydantic import BaseModel


class SubredditBase(BaseModel):
    """Base class for Subreddit model."""
    name: str
    description: str


class Subreddit(SubredditBase):
    """Database Subreddit model."""
    id: int
    user_id: int
    created_at: datetime

    class Config:
        """Database configuration."""
        orm_mode = True


class SubredditCreate(SubredditBase):
    """Subreddit creation model."""
