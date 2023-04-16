from sqlalchemy import Column, String, Integer

from src.main.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
