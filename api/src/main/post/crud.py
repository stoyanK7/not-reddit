from sqlalchemy.orm import Session

from src.main.post.model import Post as PostModel
from src.main.post.model import User as UserModel


def get_10_latest_posts(db: Session, page: int = 0):
    post_limit = 10
    offset = page * post_limit
    return db.query(PostModel) \
        .order_by(PostModel.posted_at.desc()) \
        .offset(offset) \
        .limit(post_limit) \
        .all()


def get_10_hot_posts(db: Session, page: int = 0):
    post_limit = 10
    offset = page * post_limit
    return db.query(PostModel) \
        .order_by(PostModel.votes.desc()) \
        .offset(offset) \
        .limit(post_limit) \
        .all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(PostModel).filter(PostModel.id == post_id).first()


def create_post(db: Session, post: dict):
    db_post = PostModel(**post)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post_body(db: Session, post_id: int, body: str):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.body = body
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post_silver_awards(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.silver_awards += 1
    db.commit()
    db.refresh(db_post)


def update_post_gold_awards(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.gold_awards += 1
    db.commit()
    db.refresh(db_post)


def update_post_platinum_awards(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.platinum_awards += 1
    db.commit()
    db.refresh(db_post)


def cast_upvote(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.votes += 1
    db.commit()
    db.refresh(db_post)


def cast_downvote(db: Session, post_id: int):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    db_post.votes -= 1
    db.commit()
    db.refresh(db_post)


def delete_post_by_id(db: Session, post_id: int):
    db.query(PostModel).filter(PostModel.id == post_id).delete()
    db.commit()
    return


def delete_user_posts(db: Session, username: str):
    db.query(PostModel).filter(PostModel.username == username).delete()
    db.commit()
    return


def insert_user(db: Session, username: str, oid: str):
    db_user = UserModel(username=username, oid=oid)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, oid: str):
    db.query(UserModel).filter(UserModel.oid == oid).delete()
    db.commit()
    return


def get_username_by_oid(db: Session, oid: str):
    return db.query(UserModel).filter(UserModel.oid == oid).first().username
