from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from src.main.database import Base


class Subreddit(Base):
    __tablename__ = "subreddits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
