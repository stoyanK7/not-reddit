from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from src.main.shared.database.main import get_db
from src.main.vote.schema import VoteCreate
from src.main.vote import crud
from src.main.vote.settings import settings
from src.main.vote.util import assert_is_upvote_or_downvote, get_username_from_access_token

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.post("/post", status_code=HTTP_204_NO_CONTENT)
def cast_post_vote(request: Request, body: VoteCreate, db: Session = Depends(get_db)):
    assert_is_upvote_or_downvote(body.vote_type)

    vote = body.dict()
    vote["vote_type"] = "post"
    vote["username"] = get_username_from_access_token(db=db, request=request)

    # TODO: background task event emit

    crud.cast_vote(db=db, vote=vote)
    return


@router.post("/comment", status_code=HTTP_204_NO_CONTENT)
def cast_comment_vote(request: Request, body: VoteCreate, db: Session = Depends(get_db)):
    assert_is_upvote_or_downvote(body.vote_type)

    vote = body.dict()
    vote["vote_type"] = "comment"
    vote["username"] = get_username_from_access_token(db=db, request=request)

    # TODO: background task event emit

    crud.cast_vote(db=db, vote=vote)
    return
