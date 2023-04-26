from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    posted_at: datetime
    title: str
    body: str
    username: str
    votes: int

    class Config:
        orm_mode = True


class TextPostCreate(BaseModel):
    title: str
    body: str
    username: str
