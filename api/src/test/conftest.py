"""This module is used to store pytest fixtures."""

import pytest
from .database import client, session
from src.main.post.model import Post as PostModel


@pytest.fixture
def insert_mock_posts():
    """Insert mock posts into the database."""

    def _insert_mock_posts(amount, session) -> list[PostModel]:
        posts: list[PostModel] = []
        for x in range(0, amount):
            post = {
                "title": f"Test post {x}",
                "body": f"Test body {x}"
            }
            model = PostModel(**post)
            posts.append(model)
            session.add(model)
        session.commit()
        return posts

    yield _insert_mock_posts


@pytest.fixture
def remove_json_field():
    """Remove a field from a JSON object."""

    def _remove_json_field(json_object, field_name):
        json_object.pop(field_name, None)
        return json_object

    yield _remove_json_field
