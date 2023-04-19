from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.main.database import get_db, engine
from src.main.post import crud
from src.main.post.model import Base
from src.main.post.schema import PostCreate
from src.main.auth_config import configure_cors

Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.get("/", status_code=HTTP_200_OK)
def get_10_posts(page: int = 0, db: Session = Depends(get_db)):
    # TODO: Probably should be latest posts
    return crud.get_10_posts(db=db, page=page)


@app.get("/{post_id}", status_code=HTTP_200_OK)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post_by_id(db=db, post_id=post_id)


@app.post("/", status_code=HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    # TODO: Think about handling media
    return crud.create_post(db=db, post=post)


@app.delete("/{post_id}", status_code=HTTP_204_NO_CONTENT)
def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    # TODO: ensure user is owner of post
    return crud.delete_post_by_id(db=db, post_id=post_id)
