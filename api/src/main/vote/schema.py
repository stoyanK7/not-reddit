"""This module contains the Vote schemas."""

from datetime import datetime
from pydantic import BaseModel
from .model import TargetType, VoteType


class VoteBase(BaseModel):
    """Base class for Vote model."""
    target_id: int
    target_type: TargetType
    vote_type: VoteType


class Vote(VoteBase):
    """Database vote model."""
    id: int
    user_id: int
    voted_at: datetime

    class Config:
        """Database configuration."""
        orm_mode = True


class VoteCreate(VoteBase):
    """Vote creation model."""
