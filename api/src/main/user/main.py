from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user import crud, model
from src.main.user.schema import UserCreate as UserCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/", status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    crud.create_user(db=db, user=user)
    return

@app.get("/{username}", status_code=200)
def get_user(username: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, username=username)
