import jwt
import pytest as pytest
from fastapi import status


def test_get_posts_length(client, session, insert_mock_text_posts):
    """Assert that posts length is 10."""
    insert_mock_text_posts(12, session=session)

    response = client.get("/api/post")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_get_posts_pagination(client, session, insert_mock_text_posts):
    """Assert that pagination works."""
    insert_mock_text_posts(23, session=session)

    response = client.get("/api/post?page=2")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3


def test_get_post(client, session, insert_mock_text_posts):
    """Assert that post can be fetched by id."""
    post = insert_mock_text_posts(1, session=session)[0]
    response = client.get(f"/api/post/{post.id}")

    assert response.status_code == status.HTTP_200_OK
    assert "title" in response.json().keys()


def test_create_text_post(client, session, remove_json_fields, insert_user):
    """Assert that a text post is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    body = {
        "title": "Test post",
        "body": "Test body",
    }

    jwt_token = jwt.encode({"oid": user.oid}, "secret", algorithm="HS256")
    response = client.post("/api/post/text", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.json().keys()
    assert response.json()["username"] == user.username
    assert response.json()["votes"] == 0


@pytest.mark.skip(reason="Not implemented")
def test_create_image_post(client):
    pass


def test_delete_post(client, session, insert_user, insert_post):
    """Assert that post is deleted."""
    # Insert user
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    # Insert post
    post = insert_post({
        "title": "Title",
        "body": "Body",
        "username": user.username,
    }, session=session)

    # Delete post
    jwt_token = jwt.encode({"oid": user.oid}, "secret", algorithm="HS256")
    response = client.delete(f"/api/post/{post.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_post_not_owner_of_post(client, session, insert_post, insert_user):
    # Insert users
    user_1 = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)
    user_2 = insert_user({
        "username": "amazedPotato6",
        "oid": "user 2 oid"
    }, session=session)

    # Insert post under different name
    post = insert_post({
        "title": "Title",
        "body": "Body",
        "username": user_1.username,
    }, session=session)

    # Try to delete post
    jwt_token = jwt.encode({"oid": user_2.oid}, "secret", algorithm="HS256")
    response = client.delete(f"/api/post/{post.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "You are not the owner of this post"}
