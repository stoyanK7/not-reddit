from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from src.main.shared.database.main import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    user_id = Column(Integer)
    post_id = Column(Integer)
    commented_at = Column(DateTime(timezone=True), server_default=func.now())


class User(Base):
    __tablename__ = "comment_users_oid"

    oid = Column(String, primary_key=True, unique=True, index=True)
    username = Column(String, unique=True, index=True)
