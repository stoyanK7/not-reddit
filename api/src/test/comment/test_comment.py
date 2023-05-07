import datetime

from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK, \
    HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

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
    assert response.json()["votes"] == 0
    assert session.query(CommentModel).filter_by(id=response.json()["id"]).first() is not None


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
    assert session.query(CommentModel).first() is None


def test_delete_comment(client, session, insert_user, insert_post, insert_comment, generate_jwt):
    """Assert that comment is deleted."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    comment = insert_comment({
        "body": "Test body",
        "post_id": post.post_id,
        "username": user.username
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.delete(f"/api/comment/{comment.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(CommentModel).filter_by(id=comment.id).first() is None


def test_delete_comment__not_owner_of_comment(client, session, insert_user, insert_post,
                                              insert_comment, generate_jwt):
    """Assert that comment is deleted."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    comment = insert_comment({
        "body": "Test body",
        "post_id": post.post_id,
        "username": "not owner"
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.delete(f"/api/comment/{comment.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "You are not the owner of this comment"
    assert session.query(CommentModel).filter_by(id=comment.id).first() is not None


def test_get_latest_comments_for_post_id(client, session, insert_comment):
    """Assert that latest comments are retrieved."""
    post_id = 1
    insert_comment({
        "body": "Should be second",
        "post_id": post_id,
        "commented_at": datetime.datetime(2023, 5, 4)
    }, session=session)
    insert_comment({
        "body": "Should be third",
        "post_id": post_id,
        "commented_at": datetime.datetime(2023, 5, 3)
    }, session=session)
    insert_comment({
        "post_id": post_id,
        "body": "Should be first",
        "post_id": post_id,
        "commented_at": datetime.datetime(2023, 5, 6)
    }, session=session)

    response = client.get(f"/api/comment?sort_by=latest&post_id={post_id}")

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]["body"] == "Should be first"
    assert response.json()[1]["body"] == "Should be second"
    assert response.json()[2]["body"] == "Should be third"


def test_get_hot_comments_for_post_id(client, session, insert_comment):
    """Assert that hot comments are retrieved."""
    post_id = 1
    insert_comment({
        "body": "Should be second",
        "post_id": post_id,
        "votes": 2
    }, session=session)
    insert_comment({
        "body": "Should be third",
        "post_id": post_id,
        "votes": 1
    }, session=session)
    insert_comment({
        "body": "Should be first",
        "post_id": post_id,
        "votes": 3
    }, session=session)

    response = client.get(f"/api/comment?sort_by=hot&post_id={post_id}")

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]["body"] == "Should be first"
    assert response.json()[1]["body"] == "Should be second"
    assert response.json()[2]["body"] == "Should be third"
