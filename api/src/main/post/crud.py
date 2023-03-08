from sqlalchemy.orm import Session

from .schema import PostCreate
from .model import Post as PostModel


def create_post(db: Session, post: PostCreate):
    db_post = PostModel(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
