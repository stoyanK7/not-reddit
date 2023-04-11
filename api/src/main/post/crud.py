from sqlalchemy.orm import Session
from .schema import PostCreate
from .model import Post as PostModel


def get_10_posts(db: Session, page: int = 0):
    post_limit = 10
    offset = page * post_limit
    return db.query(PostModel).offset(offset).limit(post_limit).all()


def get_post(db: Session, post_id: int):
    return db.query(PostModel).filter(PostModel.id == post_id).first()


def create_post(db: Session, post: PostCreate):
    db_post = PostModel(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db.query(PostModel).filter(PostModel.id == post_id).delete()
    db.commit()
    return
