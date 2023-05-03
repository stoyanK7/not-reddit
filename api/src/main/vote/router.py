from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from src.main.shared.database.main import get_db
from src.main.vote.schema import VoteCreate
from src.main.vote import crud
from src.main.vote.settings import settings

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.post("/post", status_code=HTTP_204_NO_CONTENT)
def cast_post_vote(body: VoteCreate, db: Session = Depends(get_db)):
    vote = body.dict()
    vote["vote_type"] = "post"
    vote["username"] = "ads"  # TODO: get from token

    # TODO: background task event emit

    crud.cast_vote(db=db, vote=vote)
    return


@router.post("/comment", status_code=HTTP_204_NO_CONTENT)
def cast_comment_vote(body: VoteCreate, db: Session = Depends(get_db)):
    vote = body.dict()
    vote["vote_type"] = "comment"
    vote["username"] = "ads"  # TODO: get from token

    # TODO: background task event emit

    crud.cast_vote(db=db, vote=vote)
    return
