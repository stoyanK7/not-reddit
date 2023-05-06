import json

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST
from aio_pika.abc import AbstractIncomingMessage

from src.main.shared.amqp.amqp_util import decode_body_and_convert_to_dict
from src.main.shared.database.main import get_db
from src.main.shared.jwt_util import get_access_token_oid
from src.main.vote import crud


def assert_is_upvote_or_downvote(vote_type: str):
    is_upvote_or_downvote = vote_type in ["up", "down"]
    if not is_upvote_or_downvote:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="vote_type must be either 'up' or 'down'",
        )


def get_username_from_access_token(db: Session, request: Request) -> str:
    oid = get_access_token_oid(request=request)
    return crud.get_username_by_oid(db=db, oid=oid)


def handle_user_registration(message: AbstractIncomingMessage):
    body = decode_body_and_convert_to_dict(message.body)
    username = body['username']
    oid = body['oid']
    db = next(get_db())
    crud.insert_user(db=db, username=username, oid=oid)


def handle_post_creation(message: AbstractIncomingMessage):
    body = decode_body_and_convert_to_dict(message.body)
    db = next(get_db())
    crud.insert_post(db=db, post=body)


def handle_comment_creation(message: AbstractIncomingMessage):
    body = decode_body_and_convert_to_dict(message.body)
    db = next(get_db())
    crud.insert_comment(db=db, comment=body)


async def emit_post_vote_casted_event(request: Request, vote: dict):
    body = json.dumps(vote)
    # TODO: move conversion of string and json.dumps to amql_util function
    await request.app.post_vote_casted_amqp_publisher.send_message(str(body))


async def emit_comment_vote_casted_event(request: Request, vote: dict):
    body = json.dumps(vote)
    # TODO: move conversion of string and json.dumps to amql_util function
    await request.app.comment_vote_casted_amqp_publisher.send_message(str(body))
