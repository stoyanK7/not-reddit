from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from src.main.comment.model import Comment as CommentModel


def test_get_comments_length(client, session, insert_post, insert_mock_comments):
    """Assert that comments length is 10."""
    post = insert_post({
        "post_id": 1
    }, session=session)

    insert_mock_comments(amount=12, post_id=post.post_id, session=session)

    response = client.get(f"/api/comment?page=0&post_id={post.post_id}")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 10


def test_get_comments_pagination(client, session, insert_post, insert_mock_comments):
    """Assert that pagination works."""
    post = insert_post({
        "post_id": 1
    }, session=session)

    insert_mock_comments(amount=23, post_id=post.post_id, session=session)

    response = client.get(f"/api/comment?page=2&post_id={post.post_id}")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 3


def test_create_comment(client, session, remove_json_fields, insert_user, insert_post,
                        generate_jwt):
    """Assert that comment is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    body = {
        "body": "Test body",
        "post_id": post.post_id
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED
    assert "id" in response.json().keys()
    assert response.json()["body"] == body["body"]
    assert response.json()["username"] == user.username


def test_create_comment_non_existing_post(client, session, remove_json_fields, insert_user,
                                          generate_jwt):
    """Assert that comment is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    body = {
        "body": "Test body",
        "post_id": 100
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Post not found"


def test_delete_comment(client, session, insert_mock_comments):
    """Assert that comment is deleted."""
    comment = insert_mock_comments(amount=1, post_id=1, session=session)[0]
    response = client.delete(f"/api/comment/{comment.id}")

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(CommentModel).filter_by(id=comment.id).first() is None
