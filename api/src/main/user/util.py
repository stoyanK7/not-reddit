import jwt
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from src.main.user.crud import get_user_by_username_or_email


def assert_is_jwt_email_same_as_provided_email(provided_email: str, request: Request):
    jwt_token = extract_token(request.headers['Authorization'])
    decoded = jwt.decode(jwt_token, options={"verify_signature": False})
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
