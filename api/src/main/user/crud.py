from sqlalchemy.orm import Session

from src.main.user.schema import UserCreate
from src.main.user.model import User as UserModel


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
