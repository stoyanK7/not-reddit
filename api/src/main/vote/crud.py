from sqlalchemy.orm import Session

from src.main.vote.model import Vote as VoteModel, User as UserModel, Post as PostModel, \
    Comment as CommentModel


def cast_vote(db: Session, vote: dict):
    db_vote = VoteModel(**vote)
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return


def insert_user(db: Session, username: str, oid: str):
    db_user = UserModel(username=username, oid=oid)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def insert_post(db: Session, post: dict):
    db_post = PostModel(post_id=post["id"])
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def insert_comment(db: Session, comment: dict):
    db_comment = CommentModel(comment_id=comment["id"])
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
