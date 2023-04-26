from fastapi import FastAPI, Depends, Request
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user.lifespan import lifespan
from src.main.user.model import Base
from src.main.user import crud
from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered
from src.main.user.util import assert_is_jwt_email_same_as_provided_email, \
    assert_is_username_and_email_not_taken, assert_is_user_exists, \
    send_successful_registration_email
from random_username.generate import generate_username

Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=lifespan)


@app.get("/{username}", status_code=HTTP_200_OK)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db=db, username=username)
    assert_is_user_exists(user)

    return user


@app.post("/", status_code=HTTP_201_CREATED)
def create_user(request: Request, body: UserCreate, db: Session = Depends(get_db)):
    # assert_is_jwt_email_same_as_provided_email(body.email, request=request)
    new_username = generate_username(1)[0]
    # assert_is_username_and_email_not_taken(username=new_username, email=body.email, db=db)

    crud.create_user(db=db, username=new_username, email=body.email)
    # TODO: notify post service about new user
    send_successful_registration_email(email=body.email)
    return


@app.post("/registered", status_code=HTTP_200_OK)
def check_if_registered(request: Request, body: UserCheckIfRegistered,
                        db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)

    registered = crud.get_user_by_email(db=db, email=body.email) is not None
    return {"registered": registered}
