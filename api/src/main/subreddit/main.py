"""This module contains the subreddit REST API endpoints."""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import SubredditCreate as SubredditCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/subreddit", status_code=201)
def create_subreddit(subreddit: SubredditCreateSchema, db: Session = Depends(get_db)):
    """Create a subreddit."""
    return crud.create_subreddit(db=db, subreddit=subreddit)
