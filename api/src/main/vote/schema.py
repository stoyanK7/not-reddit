from datetime import datetime
from pydantic import BaseModel
from src.main.vote.model import TargetType, VoteType


class VoteBase(BaseModel):
    target_id: int
    target_type: TargetType
    vote_type: VoteType


class Vote(VoteBase):
    id: int
    user_id: int
    voted_at: datetime

    class Config:
        orm_mode = True


class VoteCreate(VoteBase):
    pass
