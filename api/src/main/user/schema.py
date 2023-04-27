from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class User(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
