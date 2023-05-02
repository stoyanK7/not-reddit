from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK

from src.main.comment.model import Comment as CommentModel


def test_get_comments_length(client, session, insert_mock_comments):
    """Assert that comments length is 10."""
    insert_mock_comments(12, session=session)

    response = client.get("/api/comment")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 10


def test_get_comments_pagination(client, session, insert_mock_comments):
    """Assert that pagination works."""
    insert_mock_comments(23, session=session)

    response = client.get("/api/comment?page=2")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 3


def test_create_comment(client, session, remove_json_fields, insert_user, generate_jwt):
    """Assert that comment is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    body = {
        "body": "Test body",
        "post_id": 1
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED
    assert "id" in response.json().keys()
    assert response.json()["body"] == body["body"]
    assert response.json()["username"] == user.username


def test_delete_comment(client, session, insert_mock_comments):
    """Assert that comment is deleted."""
    comment = insert_mock_comments(1, session=session)[0]
    response = client.delete(f"/api/comment/{comment.id}")

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(CommentModel).filter_by(id=comment.id).first() is None
