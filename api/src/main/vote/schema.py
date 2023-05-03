from datetime import datetime
from pydantic import BaseModel


class VoteBase(BaseModel):
    target_id: int
    # TODO: Try enum here
    vote_type: str


class Vote(VoteBase):
    id: int
    user_id: int
    voted_at: datetime

    class Config:
        orm_mode = True


class VoteCreate(VoteBase):
    pass
