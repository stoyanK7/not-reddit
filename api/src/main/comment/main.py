"""This module contains the comment REST API endpoints."""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import Comment as CommentSchema
from .schema import CommentCreate as CommentCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=list[CommentSchema])
def get_comments(page: int = 0, db: Session = Depends(get_db)):
    """Get 10 comments."""
    return crud.get_comments(db=db, page=page)


@app.post("/", status_code=201, response_model=CommentSchema)
def create_comment(comment: CommentCreateSchema, db: Session = Depends(get_db)):
    """Create a comment."""
    return crud.create_comment(db=db, comment=comment)
