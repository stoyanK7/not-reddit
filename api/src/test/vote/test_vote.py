from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


def test_upvote_post(client, session):
    """Assert that upvoting a post works."""
    body = {
        "target_id": 1,
        "vote_type": "up"
    }

    response = client.post("/api/vote/post", json=body)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_downvote_post(client, session):
    """Assert that downvoting a post works."""
    body = {
        "target_id": 1,
        "vote_type": "down"
    }

    response = client.post("/api/vote/post", json=body)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_upvote_comment(client, session):
    """Assert that upvoting a comment works."""
    body = {
        "target_id": 1,
        "vote_type": "up"
    }

    response = client.post("/api/vote/comment", json=body)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_downvote_comment(client, session):
    """Assert that downvoting a comment works."""
    body = {
        "target_id": 1,
        "vote_type": "down"
    }

    response = client.post("/api/vote/comment", json=body)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_invalid_vote(client, session):
    """Assert that an invalid vote_type is rejected."""
    body = {
        "target_id": 1,
        "vote_type": "invalid"
    }

    response = client.post("/api/vote/post", json=body)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "vote_type must be either 'up' or 'down'"
    }
