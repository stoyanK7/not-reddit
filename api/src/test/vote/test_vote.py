from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from src.main.vote.model import Vote as VoteModel


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
    assert session.query(VoteModel).filter_by(target_id=post.post_id).first() is not None


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
    assert session.query(VoteModel).filter_by(target_id=post.post_id).first() is not None


def test_upvote_comment(client, session, insert_user, insert_comment, generate_jwt):
    """Assert that upvoting a comment works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    comment = insert_comment({
        "comment_id": 1,
    }, session=session)

    body = {
        "target_id": comment.comment_id,
        "vote_type": "up"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(VoteModel).filter_by(target_id=comment.comment_id,
                                              vote_type=body["vote_type"]).first() is not None


def test_downvote_comment(client, session, insert_user, insert_comment, generate_jwt):
    """Assert that downvoting a comment works."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    comment = insert_comment({
        "comment_id": 1,
    }, session=session)

    body = {
        "target_id": comment.comment_id,
        "vote_type": "down"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_204_NO_CONTENT
    assert session.query(VoteModel).filter_by(target_id=comment.comment_id,
                                              vote_type=body["vote_type"]).first() is not None


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


def test_upvote_post_already_upvoted(client, session, generate_jwt, insert_user, insert_vote,
                                     insert_post):
    """Assert that upvoting a post already upvoted by the user throws an exception."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    vote = insert_vote({
        "target_id": post.post_id,
        "username": user.username,
        "vote_type": "up",
        "target_type": "post"
    }, session=session)

    body = {
        "target_id": post.post_id,
        "vote_type": "up"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/post", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "Vote already casted for this post"
    }
    assert len(
        session.query(VoteModel).filter_by(target_id=vote.target_id, vote_type=vote.vote_type,
                                           target_type=vote.target_type).all()) == 1


def test_downvote_post_already_downvoted(client, session, generate_jwt, insert_user, insert_vote,
                                         insert_post):
    """Assert that downvoting a post already downvoted by the user throws an exception."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    post = insert_post({
        "post_id": 1
    }, session=session)

    vote = insert_vote({
        "target_id": post.post_id,
        "username": user.username,
        "vote_type": "down",
        "target_type": "post"
    }, session=session)

    body = {
        "target_id": post.post_id,
        "vote_type": "down"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/post", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "Vote already casted for this post"
    }
    assert len(
        session.query(VoteModel).filter_by(target_id=vote.target_id, vote_type=vote.vote_type,
                                           target_type=vote.target_type).all()) == 1


def test_upvote_comment_already_upvoted(client, session, generate_jwt, insert_user, insert_vote,
                                        insert_comment):
    """Assert that upvoting a comment already upvoted by the user throws an exception."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    comment = insert_comment({
        "comment_id": 1
    }, session=session)

    vote = insert_vote({
        "target_id": comment.comment_id,
        "username": user.username,
        "vote_type": "up",
        "target_type": "comment"
    }, session=session)

    body = {
        "target_id": comment.comment_id,
        "vote_type": "up"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "Vote already casted for this comment"
    }
    assert len(
        session.query(VoteModel).filter_by(target_id=vote.target_id, vote_type=vote.vote_type,
                                           target_type=vote.target_type).all()) == 1


def test_downvote_comment_already_downvoted(client, session, generate_jwt, insert_user, insert_vote,
                                            insert_comment):
    """Assert that downvoting a comment already downvoted by the user throws an exception."""
    user = insert_user({
        "username": "puzzledUser2",
        "oid": "user 1 oid"
    }, session=session)

    comment = insert_comment({
        "comment_id": 1
    }, session=session)

    vote = insert_vote({
        "target_id": comment.comment_id,
        "username": user.username,
        "vote_type": "up",
        "target_type": "comment"
    }, session=session)

    body = {
        "target_id": comment.comment_id,
        "vote_type": "down"
    }

    jwt_token = generate_jwt({"oid": user.oid})
    response = client.post("/api/vote/comment", json=body,
                           headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {
        "detail": "Vote already casted for this comment"
    }
    assert len(
        session.query(VoteModel).filter_by(target_id=vote.target_id, vote_type=vote.vote_type,
                                           target_type=vote.target_type).all()) == 1
