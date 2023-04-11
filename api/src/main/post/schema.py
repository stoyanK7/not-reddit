from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    body: str


class Post(PostBase):
    id: int
    posted_at: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass
