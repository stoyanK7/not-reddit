from pydantic import BaseModel


class PostBase(BaseModel):
    title: str


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass
