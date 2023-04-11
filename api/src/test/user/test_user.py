"""This module is used to test the user endpoints."""

import pytest
from starlette.status import HTTP_201_CREATED

from src.main.user.model import User as UserModel


def test_create_user(client, session, mock_user, remove_json_fields):
    """Assert that user is created."""
    body = mock_user

    response = client.post("/user", json=body)

    assert response.status_code == HTTP_201_CREATED


@pytest.mark.skip(reason="Password is not yet hashed.")
def test_create_user_password_hashed(client, session, mock_user, remove_json_fields):
    """Assert that user is created."""
    body = mock_user

    response = client.post("/user", json=body)
    user = session.query(UserModel).filter(UserModel.username == body["username"]).first()
    # Assert that password is hashed.
    assert user.password != body["password"]
