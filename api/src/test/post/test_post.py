import datetime
import os
import shutil

import pytest
from starlette.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, \
    HTTP_200_OK, HTTP_400_BAD_REQUEST

from src.main.post.model import Post as PostModel

current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)
resource_directory = f"{parent_directory}/resource"
files_directory = f"{os.path.dirname(os.path.dirname(parent_directory))}/main/post/files"


def test_get_posts_length(client, session, insert_mock_text_posts):
    """Assert that posts length is 10."""
    insert_mock_text_posts(12, session=session)

    response = client.get("/api/post")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 10


def test_get_posts_pagination(client, session, insert_mock_text_posts):
    """Assert that pagination works."""
    insert_mock_text_posts(23, session=session)

    response = client.get("/api/post?page=2")

    assert response.status_code == HTTP_200_OK
    assert len(response.json()) == 3


def test_get_latest_posts(client, session, insert_post):
    """Assert that latest posts are returned."""
    insert_post({
        "title": "Should be second",
        "posted_at": datetime.datetime(2023, 5, 4)
    }, session=session)
    insert_post({
        "title": "Should be third",
        "posted_at": datetime.datetime(2023, 5, 3)
    }, session=session)
    insert_post({
        "title": "Should be first",
        "posted_at": datetime.datetime(2023, 5, 6)
    }, session=session)

    response = client.get("/api/post?sort_by=latest")

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]["title"] == "Should be first"
    assert response.json()[1]["title"] == "Should be second"
    assert response.json()[2]["title"] == "Should be third"


def test_get_hot_posts(client, session, insert_post):
    """Assert that hot posts are returned."""
    insert_post({
        "title": "Should be second",
        "posted_at": datetime.datetime(2023, 5, 4),
        "votes": 10
    }, session=session)
    insert_post({
        "title": "Should be third",
        "posted_at": datetime.datetime(2023, 5, 3),
        "votes": 20
    }, session=session)
    insert_post({
        "title": "Should be first",
        "posted_at": datetime.datetime(2023, 5, 6),
        "votes": 5
    }, session=session)

    response = client.get("/api/post?sort_by=hot")

    assert response.status_code == HTTP_200_OK
    assert response.json()[0]["title"] == "Should be third"
    assert response.json()[1]["title"] == "Should be second"
    assert response.json()[2]["title"] == "Should be first"


def test_get_post(client, session, insert_mock_text_posts):
    """Assert that post can be fetched by id."""
    post = insert_mock_text_posts(1, session=session)[0]
    response = client.get(f"/api/post/{post.id}")

    assert response.status_code == HTTP_200_OK
    assert "title" in response.json().keys()
    assert "body" in response.json().keys()


def test_create_text_post(client, session, remove_json_fields, insert_user, generate_jwt):
    """Assert that a text post is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    body = {
        "title": "Test post",
        "body": "Test body",
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/post/text", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED
    assert "id" in response.json().keys()
    assert response.json()["title"] == body["title"]
    assert response.json()["body"] == body["body"]
    assert response.json()["username"] == user.username
    assert response.json()["votes"] == 0
    assert session.query(PostModel).filter_by(id=response.json()["id"]).first() is not None


@pytest.mark.parametrize("test_file_name",
                         ["test_image.png", "test_image.jpg", "test_video.mp4", "test_video.webm"])
def test_create_media_post(client, session, insert_user, test_file_name, generate_jwt):
    """Assert that a media post is created."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    data = {
        "title": "Test post",
    }

    test_media_path = os.path.join(resource_directory, test_file_name)
    files = [
        ("file", open(test_media_path, "rb"))
    ]

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/post/media", data=data, files=files,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_201_CREATED
    assert "id" in response.json().keys()
    assert response.json()["title"] == data["title"]
    assert str(response.json()["id"]) in response.json()["body"]
    assert response.json()["username"] == user.username
    assert session.query(PostModel).filter_by(id=response.json()["id"]).first() is not None

    uploaded_media_path = (f"{files_directory}/{response.json()['id']}."
                           f"{test_file_name.split('.')[-1]}")
    assert os.path.exists(uploaded_media_path)
    os.remove(uploaded_media_path)
    assert not os.path.exists(uploaded_media_path)


def test_create_media_post_invalid_media_type(client, session, insert_user, generate_jwt):
    """Assert that a media post is not created if the media type is invalid."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    data = {
        "title": "Test post",
    }

    test_media_path = os.path.join(parent_directory, __file__)
    files = [
        ("file", open(test_media_path, "rb"))
    ]

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/post/media", data=data, files=files,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert session.query(PostModel).first() is None


def test_delete_text_post(client, session, insert_user, insert_post, generate_jwt):
    """Assert that post is deleted."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "title": "Title",
        "body": "Body",
        "username": user.username,
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.delete(f"/api/post/{post.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(PostModel).filter_by(id=post.id).first() is None


def test_delete_text_post_not_owner_of_post(client, session, insert_post, insert_user,
                                            generate_jwt):
    """Assert that post is not deleted if user is not the owner of the post."""
    user_1 = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)
    user_2 = insert_user({
        "username": "amazedPotato6",
        "oid": "user 2 oid"
    }, session=session)

    post = insert_post({
        "title": "Title",
        "body": "Body",
        "username": user_1.username,
    }, session=session)

    jwt_token = generate_jwt({"oid": user_2.oid})
    response = client.delete(f"/api/post/{post.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "You are not the owner of this post"}
    assert session.query(PostModel).filter_by(id=post.id).first() is not None


@pytest.mark.parametrize("test_file_name",
                         ["test_image.png", "test_image.jpg", "test_video.mp4", "test_video.webm"])
def test_delete_media_post(client, session, insert_post, insert_user, test_file_name, generate_jwt):
    """Assert that media post is deleted."""
    test_media_path = os.path.join(resource_directory, test_file_name)
    uploaded_media_path = f"{files_directory}/1.{test_file_name.split('.')[-1]}"
    shutil.copy(test_media_path, uploaded_media_path)
    assert os.path.exists(uploaded_media_path)

    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "title": "Test post",
        "body": f"file://{uploaded_media_path}",
        "username": user.username,
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.delete(f"/api/post/{post.id}",
                             headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(PostModel).filter_by(id=post.id).first() is None
    assert not os.path.exists(uploaded_media_path)
