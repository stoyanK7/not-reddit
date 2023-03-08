from pydantic import BaseModel


class PostBase(BaseModel):
    """Base class for Post model."""
    title: str


class Post(PostBase):
    """Database post model."""
    id: int

    class Config:
        """Database configuration."""
        orm_mode = True


class PostCreate(PostBase):
    """Post creation model."""
