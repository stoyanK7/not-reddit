from fastapi import status
from src.main.post.model import Post as PostModel


def test_get_posts_length(client, session, insert_mock_text_posts):
    """Assert that posts length is 10."""
    insert_mock_text_posts(12, session=session)

    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_get_posts_pagination(client, session, insert_mock_text_posts):
    """Assert that pagination works."""
    insert_mock_text_posts(23, session=session)

    response = client.get("/?page=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


def test_get_post(client, session, insert_mock_text_posts):
    """Assert that post can be fetched by id."""
    post = insert_mock_text_posts(1, session=session)[0]
    response = client.get(f"/{post.id}")

    assert response.status_code == status.HTTP_200_OK
    assert {"id", "title", "body", "posted_at"} == set(response.json().keys())


def test_create_text__post(client, remove_json_fields):
    """Assert that post is created."""
    body = {
        "title": "Test post",
        "body": "Test body",
    }

    response = client.post("/text", json=body)

    assert response.status_code == status.HTTP_201_CREATED
    assert {"id", "title", "body", "posted_at"} == set(response.json().keys())
    # posted_at is a timestamp which the test cannot predict, so we remove it.
    assert remove_json_fields(response.json(), "posted_at") == {
        "id": 1,
        "title": "Test post",
        "body": "Test body"
    }


def test_delete_post(client, session, insert_mock_text_posts):
    """Assert that post is deleted."""
    post = insert_mock_text_posts(1, session=session)[0]
    response = client.delete(f"/{post.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert session.query(PostModel).filter_by(id=post.id).first() is None
