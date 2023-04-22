import json

from jwt import decode
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from src.main.user.crud import get_user_by_username_or_email
from src.main.user.rabbitmq import channel
from src.main.user.settings import settings


def assert_is_jwt_email_same_as_provided_email(provided_email: str, request: Request):
    jwt_token = extract_token(request.headers['Authorization'])
    decoded = decode(jwt_token, options={"verify_signature": False})
    is_jwt_email_same_as_body_email = decoded['preferred_username'] == provided_email

    if not is_jwt_email_same_as_body_email:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )


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


def extract_token(authorization_header: str):
    """Extracts the token from the authorization header by removing the 'Bearer ' part."""
    return authorization_header[7:]


def send_successful_registration_email(email: str):
    body = json.dumps({
        "recipients": [email],
        "content_topic": "success_register"
    })
    channel.basic_publish(exchange='', routing_key=settings.RABBITMQ_EMAIL_QUEUE, body=body)
