from typing import Annotated
from fastapi import APIRouter, UploadFile, Depends, Form, Request, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.shared.database.main import get_db
from src.main.post import crud
from src.main.post.schema import TextPostCreate
from src.main.post.settings import settings
from src.main.post.util import upload_file, assert_user_is_owner_of_post, \
    get_username_from_access_token, assert_file_type_is_allowed, \
    delete_file_from_post, construct_file_response, rename_file, emit_post_creation_event

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_200_OK)
def get_10_posts(page: int = 0, sort_by: str = "latest", db: Session = Depends(get_db)):
    if sort_by == "latest":
        return crud.get_10_latest_posts(db=db, page=page)
    elif sort_by == "hot":
        return crud.get_10_hot_posts(db=db, page=page)


@router.get("/{post_id}", status_code=HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_by_id(db=db, post_id=post_id)


@router.post("/text", status_code=HTTP_201_CREATED)
def create_text_post(request: Request, post: TextPostCreate, background_tasks: BackgroundTasks,
                     db: Session = Depends(get_db)):
    post = post.dict()
    post["post_type"] = "text"
    post["username"] = get_username_from_access_token(db=db, request=request)

    created_post = crud.create_post(db=db, post=post)

    background_tasks.add_task(emit_post_creation_event, request=request,
                              post={"id": created_post.id})

    return created_post


@router.post("/media", status_code=HTTP_201_CREATED)
async def create_media_post(request: Request, title: Annotated[str, Form()], file: UploadFile,
                            background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    assert_file_type_is_allowed(file)

    username = get_username_from_access_token(db=db, request=request)
    post = {
        "title": title,
        "post_type": "media",
        "username": username
    }
    created_post = crud.create_post(db=db, post=post)

    file = rename_file(file=file, post_id=created_post.id)
    crud.update_post_body(db=db, post_id=created_post.id, body=file.filename)

    # TODO: think about making a separate service for file compression
    background_tasks.add_task(upload_file, file=file, post_id=created_post.id)
    background_tasks.add_task(emit_post_creation_event, request=request,
                              post={"id": created_post.id})

    return created_post


@router.get("/media/{name}", status_code=HTTP_200_OK)
def get_media(name: str):
    # TODO: ensure request is valid - filetype
    # TODO: test endpoint
    return construct_file_response(name=name)


@router.delete("/{post_id}", status_code=HTTP_204_NO_CONTENT)
def delete_post_by_id(request: Request, post_id: int, db: Session = Depends(get_db)):
    assert_user_is_owner_of_post(db=db, request=request, post_id=post_id)

    post = crud.get_post_by_id(db=db, post_id=post_id)
    crud.delete_post_by_id(db=db, post_id=post_id)
    delete_file_from_post(post=post)

    return
