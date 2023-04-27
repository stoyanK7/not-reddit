import enum
from sqlalchemy import Column, Integer, DateTime, Enum
from sqlalchemy.sql import func

from src.main.database.main import Base


class VoteType(enum.Enum):
    up = "up"
    down = "down"


class TargetType(enum.Enum):
    post = "post"
    comment = "comment"


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    target_id = Column(Integer)
    target_type = Column(Enum(TargetType))
    vote_type = Column(Enum(VoteType))
    voted_at = Column(DateTime(timezone=True), server_default=func.now())
