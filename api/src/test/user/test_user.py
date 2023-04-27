from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, \
    HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
import jwt

from src.main.user.model import User as UserModel


def test_create_user(client, session, mock_user):
    """Assert that user is created."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")

    response = client.post("/api/user", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED


def test_create_user_with_different_jwt_email_and_body_email(client, session, mock_user):
    """Assert that user is not created when jwt email and body email are different."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": "different_email"}, "secret", algorithm="HS256")

    response = client.post("/api/user", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Unauthorized"}


def test_create_user_with_taken_username(client, session, mock_user_with_username):
    """Assert that user is not created when username is taken."""
    body = mock_user_with_username
    body["username"] = "taken_username"
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    response = client.post("/api/user", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_409_CONFLICT
    assert response.json() == {"detail": "Username or email already taken"}


def test_create_user_with_taken_email(client, session, mock_user_with_username):
    """Assert that user is not created when email is taken."""
    body = mock_user_with_username
    body["email"] = "taken_email"
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    response = client.post("/api/user", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_409_CONFLICT
    assert response.json() == {"detail": "Username or email already taken"}


def test_get_user_by_username(client, session, mock_user_with_username):
    """Assert that user is returned."""
    body = mock_user_with_username
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    response = client.get(f"/api/user/{body['username']}",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == body


def test_get_user_by_username_with_non_existing_user(client, session, mock_user_with_username):
    """Assert that 404 is returned when user does not exist."""
    body = mock_user_with_username
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")

    response = client.get(f"/api/user/{body['username']}",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_check_if_registered(client, session, mock_user_with_username):
    """Assert that user is registered."""
    body = mock_user_with_username
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    session.add(UserModel(**body))
    session.commit()

    response = client.post("/api/user/registered", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"registered": True}


def test_check_if_registered_not_registered(client, session, mock_user):
    """Assert that user is not registered."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")

    response = client.post("/api/user/registered", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"registered": False}


def test_check_if_registered_with_different_jwt_email_and_body_email(client, session, mock_user):
    """Assert that user is not registered when jwt email and body email are different."""
    body = mock_user
    jwt_token = jwt.encode({"preferred_username": "different_email"}, "secret", algorithm="HS256")

    response = client.post("/api/user/registered", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Unauthorized"}
