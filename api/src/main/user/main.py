"""This module contains the user REST API endpoints."""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import UserCreate as UserCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/", status_code=204)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    """Create a user."""
    crud.create_user(db=db, user=user)
    return
