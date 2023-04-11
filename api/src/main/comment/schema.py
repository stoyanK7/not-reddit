from datetime import datetime
from pydantic import BaseModel


class CommentBase(BaseModel):
    body: str
    user_id: int
    post_id: int


class Comment(CommentBase):
    id: int
    commented_at: datetime

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    pass
