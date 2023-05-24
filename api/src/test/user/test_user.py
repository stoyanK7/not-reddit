from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, \
    HTTP_204_NO_CONTENT
import jwt

from src.main.user.model import User as UserModel


def test_create_user(client, session, mock_user):
    """Assert that user is created."""
    body = mock_user

    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    response = client.post("/api/user", json=body, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED
    assert session.query(UserModel).filter_by(email=body["email"]).first() is not None


def test_create_user_with_taken_username(client, session, mock_user_with_username, insert_user):
    """Assert that user is not created when username is taken."""
    user = mock_user_with_username
    user["username"] = "taken_username"
    insert_user(user, session=session)

    jwt_token = jwt.encode({"preferred_username": user["email"]}, "secret", algorithm="HS256")
    response = client.post("/api/user", headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_409_CONFLICT
    assert response.json() == {"detail": "Username or email already taken"}
    assert len(session.query(UserModel).filter_by(email=user["email"]).all()) == 1


def test_create_user_with_taken_email(client, session, mock_user_with_username, insert_user):
    """Assert that user is not created when email is taken."""
    user = mock_user_with_username
    user["email"] = "taken_email"
    insert_user(user, session=session)

    jwt_token = jwt.encode({"preferred_username": user["email"]}, "secret", algorithm="HS256")
    response = client.post("/api/user", headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_409_CONFLICT
    assert response.json() == {"detail": "Username or email already taken"}
    assert len(session.query(UserModel).filter_by(email=user["email"]).all()) == 1


def test_get_username(client, session, mock_user_with_username, insert_user):
    """Assert that user is returned."""
    body = mock_user_with_username
    insert_user(body, session=session)

    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")
    response = client.get("/api/user/username",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"username": body["username"]}


def test_get_username_with_non_existing_user(client, session, mock_user_with_username):
    """Assert that 404 is returned when user does not exist."""
    body = mock_user_with_username
    jwt_token = jwt.encode({"preferred_username": body["email"]}, "secret", algorithm="HS256")

    response = client.get("/api/user/username",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_check_if_registered(client, session, mock_user_with_username):
    """Assert that user is registered."""
    user = mock_user_with_username
    session.add(UserModel(**user))
    session.commit()

    jwt_token = jwt.encode({"preferred_username": user["email"]}, "secret", algorithm="HS256")
    response = client.get("/api/user/registered",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"registered": True}


def test_check_if_registered_not_registered(client, session, mock_user):
    """Assert that user is not registered."""
    user = mock_user
    jwt_token = jwt.encode({"preferred_username": user["email"]}, "secret", algorithm="HS256")

    response = client.get("/api/user/registered",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_200_OK
    assert response.json() == {"registered": False}


def test_delete_user(client, session, mock_user_with_username):
    """Assert that deleting a user works."""
    user = mock_user_with_username
    session.add(UserModel(**user))
    session.commit()

    jwt_token = jwt.encode({"preferred_username": user["email"]}, "secret", algorithm="HS256")
    response = client.delete("/api/user",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(UserModel).filter_by(email=user["email"]).first() is None


def test_delete_user_non_existing_user(client, session):

    jwt_token = jwt.encode({"preferred_username": "nonexistingemail"}, "secret", algorithm="HS256")
    response = client.delete("/api/user",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}
