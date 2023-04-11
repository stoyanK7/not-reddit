from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from . import crud, model
from .schema import UserCreate as UserCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter(prefix="/user")


@router.post("/", status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    crud.create_user(db=db, user=user)
    return


app.include_router(router)
