from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


def test_upvote_post(client, session, insert_user, insert_post, generate_jwt):
    """Assert that upvoting a post works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    body = {
        "target_id": post.post_id,
        "vote_type": "up"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/post", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT


def test_downvote_post(client, session, insert_user, insert_post, generate_jwt):
    """Assert that downvoting a post works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    body = {
        "target_id": post.post_id,
        "vote_type": "down"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/post", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT


def test_upvote_comment(client, session, insert_user, insert_comment, generate_jwt):
    """Assert that upvoting a comment works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    insert_comment({
        "comment_id": 1,
    }, session=session)

    body = {
        "target_id": 1,
        "vote_type": "up"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT


def test_downvote_comment(client, session, insert_user, insert_comment, generate_jwt):
    """Assert that downvoting a comment works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    insert_comment({
        "comment_id": 1,
    }, session=session)

    body = {
        "target_id": 1,
        "vote_type": "down"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

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


def test_get_post_vote(client, session, generate_jwt, insert_user, insert_vote):
    """Assert that getting a post vote works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    insert_vote({
        "target_id": 1,
        "username": user.username,
        "vote_type": "up",
        "target_type": "post"
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.get("/api/vote/post/1",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 200
    assert "id" in response.json().keys()


def test_get_post_vote_non_existing_vote(client, session, generate_jwt, insert_user):
    """Assert that getting a post vote works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.get("/api/vote/post/1",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Vote not found"
    }


def test_get_comment_vote(client, session, generate_jwt, insert_user, insert_vote):
    """Assert that getting a comment vote works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    insert_vote({
        "target_id": 1,
        "username": user.username,
        "vote_type": "up",
        "target_type": "comment"
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.get("/api/vote/comment/1",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 200
    assert "id" in response.json().keys()


def test_get_comment_vote_non_existing_vote(client, session, generate_jwt, insert_user):
    """Assert that getting a comment vote works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.get("/api/vote/comment/1",
                          headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Vote not found"
    }
