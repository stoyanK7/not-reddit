"""This module is used to test the post endpoints."""

from fastapi import status


def test_upvote_post(client, session):
    """Assert that upvoting a post works."""
    body = {
        "target_id": 1,
        "target_type": "post",
        "vote_type": "up"
    }

    response = client.post("/vote", json=body)

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_downvote_post(client, session):
    """Assert that downvoting a post works."""
    body = {
        "target_id": 1,
        "target_type": "post",
        "vote_type": "down"
    }

    response = client.post("/vote", json=body)

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_upvote_comment(client, session):
    """Assert that upvoting a comment works."""
    body = {
        "target_id": 1,
        "target_type": "comment",
        "vote_type": "up"
    }

    response = client.post("/vote", json=body)

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_downvote_comment(client, session):
    """Assert that downvoting a comment works."""
    body = {
        "target_id": 1,
        "target_type": "comment",
        "vote_type": "down"
    }

    response = client.post("/vote", json=body)

    assert response.status_code == status.HTTP_204_NO_CONTENT
