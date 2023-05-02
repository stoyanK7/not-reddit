from fastapi import status
from src.main.comment.model import Comment as CommentModel


def test_get_comments_length(client, session, insert_mock_comments):
    """Assert that comments length is 10."""
    insert_mock_comments(12, session=session)

    response = client.get("/api/comment")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_get_comments_pagination(client, session, insert_mock_comments):
    """Assert that pagination works."""
    insert_mock_comments(23, session=session)

    response = client.get("/api/comment?page=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


def test_create_comment(client, remove_json_fields):
    """Assert that comment is created."""
    body = {
        "body": "Test body",
        "user_id": 1,
        "post_id": 1
    }

    response = client.post("/api/comment", json=body)

    assert response.status_code == status.HTTP_201_CREATED
    assert {"id", "user_id", "post_id", "body", "commented_at"} == set(response.json().keys())
    # commented_at is a timestamp which the test cannot predict, so we remove it.
    assert remove_json_fields(response.json(), "commented_at") == {
        "id": 1,
        "body": "Test body",
        "user_id": 1,
        "post_id": 1
    }


def test_delete_comment(client, session, insert_mock_comments):
    """Assert that comment is deleted."""
    comment = insert_mock_comments(1, session=session)[0]
    response = client.delete(f"/api/comment/{comment.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert session.query(CommentModel).filter_by(id=comment.id).first() is None
