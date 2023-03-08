from sqlalchemy import Column, String, Integer

from src.main.database import Base


class Post(Base):
    """Post model."""

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
