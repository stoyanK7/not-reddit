"""This module contains the User CRUD operations."""

from sqlalchemy.orm import Session
from .schema import UserCreate
from .model import User as UserModel


def create_user(db: Session, user: UserCreate):
    """Create a new user."""
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
