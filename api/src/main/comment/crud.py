from sqlalchemy.orm import Session

from src.main.comment.schema import CommentCreate
from src.main.comment.model import Comment as CommentModel, User as UserModel


def get_10_comments(db: Session, page: int = 0):
    comment_limit = 10
    offset = page * comment_limit
    return db.query(CommentModel).offset(offset).limit(comment_limit).all()


def create_comment(db: Session, comment: CommentCreate):
    db_comment = CommentModel(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db.query(CommentModel).filter(CommentModel.id == comment_id).delete()
    db.commit()
    return


def insert_user(db: Session, username: str, oid: str):
    db_user = UserModel(username=username, oid=oid)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
