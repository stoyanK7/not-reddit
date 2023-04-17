from sqlalchemy import Column, String, Integer

from src.main.database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
