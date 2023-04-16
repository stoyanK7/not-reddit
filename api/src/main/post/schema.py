from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    posted_at: datetime
    title: str
    body: str
    # user_id: int
    # subreddit_id: int

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    body: str
    # user_id: int
    # subreddit_id: int
