from sqlalchemy import Column, String

from src.main.database.main import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, primary_key=True)
    email = Column(String, unique=True, index=True)
