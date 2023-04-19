from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.subreddit import crud, model
from src.main.subreddit.schema import SubredditCreate as SubredditCreateSchema
from src.main.auth_config import configure_cors, azure_scheme

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.post("/", status_code=201)
def create_subreddit(subreddit: SubredditCreateSchema, db: Session = Depends(get_db)):
    return crud.create_subreddit(db=db, subreddit=subreddit)
