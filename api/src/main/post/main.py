from fastapi import FastAPI, Depends, UploadFile
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.database import get_db, engine
from src.main.post import crud
from src.main.post.lifespan import lifespan
from src.main.post.model import Base
from src.main.post.schema import TextPostCreate
from src.main.post.util import upload_file

Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=lifespan)


@app.get("/", status_code=HTTP_200_OK)
def get_10_posts(page: int = 0, db: Session = Depends(get_db)):
    # TODO: Probably should be latest posts
    return crud.get_10_posts(db=db, page=page)


@app.get("/{post_id}", status_code=HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_by_id(db=db, post_id=post_id)


@app.post("/text", status_code=HTTP_201_CREATED)
def create_text_post(post: TextPostCreate, db: Session = Depends(get_db)):
    post.username = "test"
    # TODO: get username from token
    return crud.create_post(db=db, post=post)


@app.post("/image")
async def create_image_post(file: UploadFile):
    # TODO: make one with create_post and make file optional
    # TODO: check for file type
    # TODO: assert is valid media file
    await upload_file(file)
    return {"info": f"file '{file.filename}' saved."}


@app.delete("/{post_id}", status_code=HTTP_204_NO_CONTENT)
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    # TODO: ensure user is owner of post
    return crud.delete_post_by_id(db=db, post_id=post_id)
