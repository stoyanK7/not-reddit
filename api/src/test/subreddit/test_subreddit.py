"""This module is used to test the subreddit endpoints."""

from fastapi import status


def test_create_subreddit(client, remove_json_fields):
    """Assert that creating a subreddit works."""
    body = {
        "name": "test",
        "description": "test"
    }

    response = client.post("/subreddit", json=body)

    assert response.status_code == status.HTTP_201_CREATED
    assert {"id", "name", "description", "user_id", "created_at"} == set(response.json().keys())
    # posted_at is a timestamp which the test cannot predict, so we remove it.
    assert remove_json_fields(response.json(), "created_at", "user_id", "id") == {
        "name": "test",
        "description": "test"
    }
