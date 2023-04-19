from starlette.status import HTTP_201_CREATED
import jwt

from src.main.user.model import User as UserModel


def test_create_user(client, session, mock_user, remove_json_fields):
    """Assert that user is created."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")

    response = client.post("/", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED


def test_create_user_with_different_jwt_email_and_body_email(client, session, mock_user):
    """Assert that user is not created when jwt email and body email are different."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": "different_email"}, "secret", algorithm="HS256")

    response = client.post("/", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


def test_create_user_with_taken_username(client, session, mock_user):
    """Assert that user is not created when username is taken."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    response = client.post("/", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 409
    assert response.json() == {"detail": "Username or email already taken"}


def test_create_user_with_taken_email(client, session, mock_user):
    """Assert that user is not created when email is taken."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    body["username"] = "different_username"
    response = client.post("/", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 409
    assert response.json() == {"detail": "Username or email already taken"}
