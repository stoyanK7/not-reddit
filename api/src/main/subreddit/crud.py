"""This module contains the Subreddit CRUD operations."""

from sqlalchemy.orm import Session
from .schema import SubredditCreate
from .model import Subreddit as SubredditModel


def create_subreddit(db: Session, subreddit: SubredditCreate) -> SubredditModel:
    """Create a subreddit."""
    db_subreddit = SubredditModel(**subreddit.dict())
    db.add(db_subreddit)
    db.commit()
    db.refresh(db_subreddit)
    return db_subreddit
