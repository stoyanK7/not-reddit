from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK

from src.main.shared.database.main import get_db
from src.main.vote.schema import VoteCreate
from src.main.vote import crud
from src.main.vote.settings import settings
from src.main.vote.util import assert_is_upvote_or_downvote, get_username_from_access_token, \
    emit_post_vote_casted_event, emit_comment_vote_casted_event, assert_vote_exists, \
    assert_vote_not_already_casted

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.post("/post", status_code=HTTP_204_NO_CONTENT)
def cast_post_vote(request: Request, body: VoteCreate, background_tasks: BackgroundTasks,
                   db: Session = Depends(get_db)):
    assert_is_upvote_or_downvote(body.vote_type)

    vote = body.dict()
    vote["target_type"] = "post"
    vote["username"] = get_username_from_access_token(db=db, request=request)

    assert_vote_not_already_casted(db=db, vote=vote)

    background_tasks.add_task(emit_post_vote_casted_event, request=request,
                              vote={"post_id": vote["target_id"], "vote_type": vote["vote_type"]})

    crud.cast_vote(db=db, vote=vote)
    return


@router.post("/comment", status_code=HTTP_204_NO_CONTENT)
def cast_comment_vote(request: Request, body: VoteCreate, background_tasks: BackgroundTasks,
                      db: Session = Depends(get_db)):
    assert_is_upvote_or_downvote(body.vote_type)

    vote = body.dict()
    vote["target_type"] = "comment"
    vote["username"] = get_username_from_access_token(db=db, request=request)

    assert_vote_not_already_casted(db=db, vote=vote)

    background_tasks.add_task(emit_comment_vote_casted_event, request=request,
                              vote={"comment_id": vote["target_id"],
                                    "vote_type": vote["vote_type"]})

    crud.cast_vote(db=db, vote=vote)
    return


@router.get("/post/{post_id}", status_code=HTTP_200_OK)
def get_post_vote(request: Request, post_id: int, db: Session = Depends(get_db)):
    username = get_username_from_access_token(db=db, request=request)

    vote = crud.get_vote(db=db, target_id=post_id, target_type="post", username=username)
    assert_vote_exists(vote)

    return vote


@router.get("/comment/{comment_id}", status_code=HTTP_200_OK)
def get_comment_vote(request: Request, comment_id: int, db: Session = Depends(get_db)):
    username = get_username_from_access_token(db=db, request=request)

    vote = crud.get_vote(db=db, target_id=comment_id, target_type="comment", username=username)
    assert_vote_exists(vote)

    return vote
