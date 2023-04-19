from fastapi import FastAPI, Depends, Request
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user.model import Base
from src.main.user import crud
from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered
from src.main.auth_config import configure_cors, azure_scheme
from src.main.user.util import assert_is_jwt_email_same_as_provided_email, \
    assert_is_username_and_email_not_taken, assert_is_user_exists

Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.get("/{username}", status_code=HTTP_200_OK, dependencies=[Depends(azure_scheme)])
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db=db, username=username)
    assert_is_user_exists(user)

    return user


@app.post("/", status_code=HTTP_201_CREATED, dependencies=[Depends(azure_scheme)])
def create_user(request: Request, body: UserCreate, db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)
    assert_is_username_and_email_not_taken(body.username, body.email, db=db)

    crud.create_user(db=db, user=body)
    return


@app.post("/registered", status_code=HTTP_200_OK, dependencies=[Depends(azure_scheme)])
def check_if_registered(request: Request, body: UserCheckIfRegistered,
                        db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)

    registered = crud.get_user_by_email(db=db, email=body.email) is not None
    return {"registered": registered}
