from sqlalchemy.orm import Session

from src.main.user.schema import UserCreate
from src.main.user.model import User as UserModel


def create_user(db: Session, user: UserCreate) -> UserModel:
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_email(db: Session, email: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_username_or_email(db: Session, username: str, email: str) -> UserModel:
    return db.query(UserModel)\
        .filter((UserModel.username == username) or (UserModel.email == email)).first()
