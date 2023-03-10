"""This module contains the Post CRUD operations."""

from sqlalchemy.orm import Session
from .schema import PostCreate
from .model import Post as PostModel


def get_posts(db: Session, page: int = 0):
    """Get 10 posts."""
    post_limit = 10
    offset = page * post_limit
    return db.query(PostModel).offset(offset).limit(post_limit).all()


def get_post(db: Session, post_id: int):
    """Get a post."""
    return db.query(PostModel).filter(PostModel.id == post_id).first()


def create_post(db: Session, post: PostCreate):
    """Create a new post."""
    db_post = PostModel(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
