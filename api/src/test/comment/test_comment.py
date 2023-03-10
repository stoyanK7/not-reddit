"""This module is used to test the comment endpoints."""

from fastapi import status


def test_get_comments_length(client, session, insert_mock_comments):
    """Assert that comments length is 10."""
    insert_mock_comments(12, session=session)

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_get_comments_pagination(client, session, insert_mock_comments):
    """Assert that pagination works."""
    insert_mock_comments(23, session=session)

    response = client.get("/?page=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


def test_create_comment(client, remove_json_field):
    """Assert that comment is created."""
    body = {
        "body": "Test body",
        "user_id": 1,
        "post_id": 1
    }

    response = client.post("/", json=body)

    assert response.status_code == status.HTTP_201_CREATED
    assert {"id", "user_id", "post_id", "body", "commented_at"} == set(response.json().keys())
    # commented_at is a timestamp which the test cannot predict, so we remove it.
    assert remove_json_field(response.json(), "commented_at") == {
        "id": 1,
        "body": "Test body",
        "user_id": 1,
        "post_id": 1
    }
