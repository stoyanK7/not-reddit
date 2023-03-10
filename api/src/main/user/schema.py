from pydantic import BaseModel


class UserBase(BaseModel):
    """Base class for User model."""
    username: str
    email: str


class User(UserBase):
    """Database post model."""
    id: int
    password: str

    class Config:
        """Database configuration."""
        orm_mode = True


class UserCreate(UserBase):
    """User creation model."""
    password: str
