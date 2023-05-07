from sqlalchemy.orm import Session

from src.main.comment.model import Comment as CommentModel, User as UserModel, Post as PostModel


def get_10_latest_comments_for_post(db: Session, post_id: int, page: int = 0):
    post_limit = 10
    offset = page * post_limit
    return db.query(CommentModel) \
        .filter(CommentModel.post_id == post_id) \
        .order_by(CommentModel.commented_at.desc()) \
        .offset(offset) \
        .limit(post_limit) \
        .all()


def get_10_hot_comments_for_post(db: Session, post_id: int, page: int = 0):
    post_limit = 10
    offset = page * post_limit
    return db.query(CommentModel) \
        .filter(CommentModel.post_id == post_id) \
        .order_by(CommentModel.votes.desc()) \
        .offset(offset) \
        .limit(post_limit) \
        .all()


def get_comment_by_id(db: Session, comment_id: int):
    return db.query(CommentModel).filter(CommentModel.id == comment_id).first()


def create_comment(db: Session, comment: dict):
    db_comment = CommentModel(**comment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def cast_upvote(db: Session, comment_id: int):
    db_post = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    db_post.votes += 1
    db.commit()
    db.refresh(db_post)


def cast_downvote(db: Session, comment_id: int):
    db_post = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    db_post.votes -= 1
    db.commit()
    db.refresh(db_post)


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


def get_username_by_oid(db: Session, oid: str):
    return db.query(UserModel).filter(UserModel.oid == oid).first().username


def insert_post(db: Session, post: dict):
    db_post = PostModel(post_id=post["id"])
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post_by_id(db: Session, post_id: int):
    return db.query(PostModel).filter(PostModel.post_id == post_id).first()
