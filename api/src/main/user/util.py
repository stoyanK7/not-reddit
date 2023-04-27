import json

from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from src.main.shared.jwt_util import get_jwt_token
from src.main.user.crud import get_user_by_username_or_email


def assert_is_username_and_email_not_taken(username: str, email: str, db: Session):
    is_username_or_email_taken = get_user_by_username_or_email(db=db, username=username,
                                                               email=email)
    if is_username_or_email_taken:
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="Username or email already taken"
        )


def assert_is_user_exists(user):
    if not user:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found"
        )


async def emit_successful_registration_event(request: Request, email: str, oid: str, username: str):
    body = json.dumps({
        "recipients": [email],
        "content_topic": "successful_registration",
        "oid": oid,
        "username": username
    })
    await request.app.successful_registration_amqp_publisher.send_message(str(body))


def get_access_token_oid(request: Request) -> str:
    token = get_jwt_token(request)
    return token.get('oid')


def get_access_token_preferred_username(request: Request) -> str:
    token = get_jwt_token(request)
    return token.get('preferred_username')
