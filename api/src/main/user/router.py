from fastapi import APIRouter, Depends, Request
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from sqlalchemy.orm import Session

from src.main.database import get_db
from src.main.user.settings import settings
from src.main.user.util import assert_is_jwt_email_same_as_provided_email, \
    assert_is_username_and_email_not_taken, assert_is_user_exists, \
    emit_successful_registration_event, get_access_token_oid
from random_username.generate import generate_username
from src.main.user import crud
from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("/{username}", status_code=HTTP_200_OK)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db=db, username=username)
    assert_is_user_exists(user)

    return user


@router.post("", status_code=HTTP_201_CREATED)
async def create_user(request: Request, body: UserCreate, db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)
    new_username = generate_username(1)[0]
    assert_is_username_and_email_not_taken(username=new_username, email=body.email, db=db)

    crud.create_user(db=db, username=new_username, email=body.email)

    oid = get_access_token_oid(request)
    await emit_successful_registration_event(request=request, email=body.email, oid=oid,
                                             username=new_username)
    return


@router.post("/registered", status_code=HTTP_200_OK)
def check_if_registered(request: Request, body: UserCheckIfRegistered,
                        db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)

    registered = crud.get_user_by_email(db=db, email=body.email) is not None
    return {"registered": registered}
