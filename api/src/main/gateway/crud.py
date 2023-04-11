"""This module contains the Auth CRUD operations."""

from sqlalchemy.orm import Session
from .model import Auth as AuthModel


def get_user(db: Session, username: str):
    """Get a user by username."""
    return db.query(AuthModel).filter(AuthModel.username == username).first()
