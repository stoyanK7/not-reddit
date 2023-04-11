from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user import crud, model
from src.main.user.hash import get_password_hash
from src.main.user.schema import UserCreate as UserCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter(prefix="/user")


@router.post("/", status_code=201)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user.password = get_password_hash(user.password)
    crud.create_user(db=db, user=user)
    return


app.include_router(router)
