"""This module is used for database connection and session management."""

from sqlalchemy import create_engine
from sqlalchemy.exc import ArgumentError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.main.env import get_env


def create_db_engine():
    """
    Create a database engine.

    Returns:
        Engine: A database engine.
    """
    database_url = f"{get_env('DB_DIALECT')}:" \
                   f"//{get_env('DB_USER')}:{get_env('DB_PASSWORD')}" \
                   f"@{get_env('DB_HOST')}:{get_env('DB_PORT')}" \
                   f"/{get_env('DB_NAME')}"

    try:
        # Try to connect to the database.
        db_engine = create_engine(database_url)
    except ArgumentError:
        # Fall back to in-memory database.
        db_engine = create_engine("sqlite:///:memory:",
                                  connect_args={"check_same_thread": False},
                                  poolclass=StaticPool)
    return db_engine


def get_db():
    """
    Get a database session.

    Returns:
        SessionLocal: A database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
