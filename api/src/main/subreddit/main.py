from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.subreddit import crud, model
from src.main.subreddit.schema import SubredditCreate as SubredditCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/", status_code=201)
def create_subreddit(subreddit: SubredditCreateSchema, db: Session = Depends(get_db)):
    return crud.create_subreddit(db=db, subreddit=subreddit)
