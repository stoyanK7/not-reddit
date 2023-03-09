"""This module is used to test the post endpoints."""

from fastapi import status


def test_get_posts_length(client, session, insert_mock_posts):
    """Assert that posts length is 10."""
    insert_mock_posts(12, session=session)

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_get_posts_pagination(client, session, insert_mock_posts):
    """Assert that pagination works."""
    insert_mock_posts(23, session=session)

    response = client.get("/?page=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


def test_get_post(client, session, insert_mock_posts):
    """Assert that post can be fetched by id."""
    post = insert_mock_posts(1, session=session)[0]
    response = client.get(f"/{post.id}")

    assert response.status_code == status.HTTP_200_OK
    assert {"id", "title", "body", "posted_at"} == set(response.json().keys())


def test_create_post(client, remove_json_field):
    """Assert that post is created."""
    body = {
        "title": "Test post",
        "body": "Test body",
    }

    response = client.post("/", json=body)

    assert response.status_code == status.HTTP_201_CREATED
    assert {"id", "title", "body", "posted_at"} == set(response.json().keys())
    # posted_at is a timestamp which the test cannot predict, so we remove it.
    assert remove_json_field(response.json(), "posted_at") == {
        "id": 1,
        "title": "Test post",
        "body": "Test body"
    }
