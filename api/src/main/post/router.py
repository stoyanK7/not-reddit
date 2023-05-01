from typing import Annotated
from fastapi import APIRouter, UploadFile, Depends, Form, Request, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.shared.database.main import get_db
from src.main.post import crud
from src.main.post.schema import TextPostCreate
from src.main.post.settings import settings
from src.main.post.util import upload_file, assert_user_is_owner_of_post, \
    get_username_from_access_token, assert_file_type_is_allowed, determine_media_url, \
    delete_file_from_post, construct_file_response, rename_file

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_200_OK)
def get_10_posts(page: int = 0, db: Session = Depends(get_db)):
    # TODO: Probably should be latest posts
    return crud.get_10_posts(db=db, page=page)


@router.get("/{post_id}", status_code=HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_by_id(db=db, post_id=post_id)


@router.post("/text", status_code=HTTP_201_CREATED)
def create_text_post(request: Request, post: TextPostCreate, db: Session = Depends(get_db)):
    post = post.dict()
    post["post_type"] = "text"
    post["username"] = get_username_from_access_token(db=db, request=request)

    return crud.create_post(db=db, post=post)


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
    media_url = determine_media_url(file=file)
    crud.update_post_body(db=db, post_id=created_post.id, body=media_url)

    # TODO: think about making a separate service for file compression
    background_tasks.add_task(upload_file, file=file, post_id=created_post.id)

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
