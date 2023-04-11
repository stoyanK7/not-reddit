"""This module contains the Auth model."""

from sqlalchemy import Column, String, Integer
from src.main.database import Base


class Auth(Base):
    """Auth model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
