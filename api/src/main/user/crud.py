from sqlalchemy.orm import Session

from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered
from src.main.user.model import User as UserModel


def create_user(db: Session, user: UserCreate) -> UserModel:
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == username).first()


def check_if_registered(db: Session, email: str) -> bool:
    return db.query(UserModel).filter(UserModel.email == email).first() is not None
