"""This module contains the post REST API endpoints."""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import Post as PostSchema
from .schema import PostCreate as PostCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=list[PostSchema])
def get_posts(page: int = 0, db: Session = Depends(get_db)):
    """Get 10 posts."""
    return crud.get_posts(db=db, page=page)


@app.get("/{post_id}", response_model=PostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    """Get a post."""
    return crud.get_post(db=db, post_id=post_id)


@app.post("/", status_code=201, response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    """Create a post."""
    return crud.create_post(db=db, post=post)


@app.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """Delete a post."""
    return crud.delete_post(db=db, post_id=post_id)
