from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.vote import crud, model
from src.main.vote.schema import VoteCreate as VoteCreateSchema
from src.main.auth_config import configure_cors, azure_scheme

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.post("/", status_code=204)
def cast_vote(vote: VoteCreateSchema, db: Session = Depends(get_db)):
    crud.cast_vote(db=db, vote=vote)
    return
