from datetime import datetime
from pydantic import BaseModel


class SubredditBase(BaseModel):
    name: str
    description: str


class Subreddit(SubredditBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class SubredditCreate(SubredditBase):
    pass
