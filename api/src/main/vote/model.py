from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func

from src.main.shared.database.main import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    target_id = Column(Integer, index=True)
    target_type = Column(String, index=True)
    vote_type = Column(String, index=True)
    voted_at = Column(DateTime(timezone=True), server_default=func.now())
