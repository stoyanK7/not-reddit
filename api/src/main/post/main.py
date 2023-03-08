from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine

from . import crud, model
from .schema import Post as PostSchema
from .schema import PostCreate as PostCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=List[PostSchema])
def get_posts():
    """Get all posts."""
    return {"message": "All posts"}


@app.post("/", response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    """Create a post."""
    return crud.create_post(db=db, post=post)
