from fastapi import Request, HTTPException
from aio_pika.abc import AbstractIncomingMessage
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from src.main.comment import crud
from src.main.shared.amqp.amqp_util import decode_body_and_convert_to_dict
from src.main.shared.database.main import get_db
from src.main.shared.jwt_util import get_access_token_oid


def handle_user_registration(message: AbstractIncomingMessage):
    body = decode_body_and_convert_to_dict(message.body)
    username = body['username']
    oid = body['oid']
    db = next(get_db())
    crud.insert_user(db=db, username=username, oid=oid)


def get_username_from_access_token(db: Session, request: Request) -> str:
    oid = get_access_token_oid(request=request)
    return crud.get_username_by_oid(db=db, oid=oid)


def handle_post_creation(message: AbstractIncomingMessage):
    body = decode_body_and_convert_to_dict(message.body)
    db = next(get_db())
    crud.insert_post(db=db, post=body)


def assert_post_exists(db: Session, post_id: int):
    post_exists = crud.get_post_by_id(db=db, post_id=post_id)
    if not post_exists:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
