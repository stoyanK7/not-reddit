from typing import Annotated
from fastapi import APIRouter, UploadFile, Depends, Form, Request
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.shared.database.main import get_db
from src.main.post import crud
from src.main.post.schema import TextPostCreate
from src.main.post.settings import settings
from src.main.post.util import upload_file, assert_user_is_owner_of_post

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("", status_code=HTTP_200_OK)
def get_10_posts(page: int = 0, db: Session = Depends(get_db)):
    # TODO: Probably should be latest posts
    return crud.get_10_posts(db=db, page=page)


@router.get("/{post_id}", status_code=HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_by_id(db=db, post_id=post_id)


@router.post("/text", status_code=HTTP_201_CREATED)
def create_text_post(post: TextPostCreate, db: Session = Depends(get_db)):
    post = post.dict()
    post["username"] = "asd"
    post["type"] = "text"
    # TODO: get username from tokena
    return crud.create_post(db=db, post=post)


@router.post("/image")
async def create_image_post(title: Annotated[str, Form()], file: UploadFile):
    # TODO: make one with create_post and make file optional
    # TODO: check for file type
    # TODO: assert is valid media file
    await upload_file(file)
    return {"info": f"file '{file.filename}' saved."}


@router.delete("/{post_id}", status_code=HTTP_204_NO_CONTENT)
def delete_post_by_id(request: Request, post_id: int, db: Session = Depends(get_db)):
    assert_user_is_owner_of_post(db=db, request=request, post_id=post_id)

    crud.delete_post_by_id(db=db, post_id=post_id)
    return
