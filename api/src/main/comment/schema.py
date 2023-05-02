from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    body: str
    post_id: int


class Comment(CommentBase):
    id: int
    username: str
    commented_at: datetime

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    pass
