"""This module contains the Comment CRUD operations."""

from sqlalchemy.orm import Session
from .schema import CommentCreate
from .model import Comment as CommentModel


def get_comments(db: Session, page: int = 0):
    """Get 10 comments."""
    comment_limit = 10
    offset = page * comment_limit
    return db.query(CommentModel).offset(offset).limit(comment_limit).all()


def create_comment(db: Session, comment: CommentCreate):
    """Create a new comment."""
    db_comment = CommentModel(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
