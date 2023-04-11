from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import VoteCreate as VoteCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/vote", status_code=204)
def cast_vote(vote: VoteCreateSchema, db: Session = Depends(get_db)):
    crud.cast_vote(db=db, vote=vote)
    return
