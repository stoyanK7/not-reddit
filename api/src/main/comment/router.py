from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.comment import crud
from src.main.comment.schema import CommentCreate
from src.main.comment.settings import settings
from src.main.comment.util import get_username_from_access_token, assert_post_exists, \
    assert_user_is_owner_of_comment, emit_comment_created_event
from src.main.shared.database.main import get_db

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_200_OK)
def get_10_comments_for_post(post_id: int, page: int = 0, sort_by: str = "hot",
                             db: Session = Depends(get_db)):
    if sort_by == "latest":
        return crud.get_10_latest_comments_for_post(db=db, page=page, post_id=post_id)
    elif sort_by == "hot":
        return crud.get_10_hot_comments_for_post(db=db, page=page, post_id=post_id)


@router.post("", status_code=HTTP_201_CREATED)
def create_comment(request: Request, comment: CommentCreate, background_tasks: BackgroundTasks,
                   db: Session = Depends(get_db)):
    assert_post_exists(db=db, post_id=comment.post_id)

    comment = comment.dict()
    comment["username"] = get_username_from_access_token(db=db, request=request)
    created_comment = crud.create_comment(db=db, comment=comment)

    background_tasks.add_task(emit_comment_created_event, request=request,
                              comment={"id": created_comment.id})

    return created_comment


@router.delete("/{comment_id}", status_code=HTTP_204_NO_CONTENT)
def delete_comment(request: Request, comment_id: int, db: Session = Depends(get_db)):
    assert_user_is_owner_of_comment(db=db, request=request, comment_id=comment_id)

    crud.delete_comment(db=db, comment_id=comment_id)
    # TODO: emit event

    return
