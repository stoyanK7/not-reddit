from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


def assert_is_upvote_or_downvote(vote_type: str):
    is_upvote_or_downvote = vote_type in ["up", "down"]
    if not is_upvote_or_downvote:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="vote_type must be either 'up' or 'down'",
        )
