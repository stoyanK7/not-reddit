from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.comment import crud
from src.main.comment.schema import CommentCreate
from src.main.comment.settings import settings
from src.main.comment.util import get_username_from_access_token
from src.main.shared.database.main import get_db

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("/", status_code=HTTP_200_OK)
def get_10_comments(page: int = 0, db: Session = Depends(get_db)):
    # TODO: Probably should be latest or most-upvoted comments
    return crud.get_10_comments(db=db, page=page)


@router.post("/", status_code=HTTP_201_CREATED)
def create_comment(request: Request, comment: CommentCreate, db: Session = Depends(get_db)):
    # TODO: Assert that post exists
    comment = comment.dict()
    comment["username"] = get_username_from_access_token(db=db, request=request)

    return crud.create_comment(db=db, comment=comment)


@router.delete("/{comment_id}", status_code=HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    # TODO: assert user is owner of comment
    return crud.delete_comment(db=db, comment_id=comment_id)
