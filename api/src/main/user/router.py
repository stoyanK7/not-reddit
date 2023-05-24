from fastapi import APIRouter, Depends, Request, BackgroundTasks
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session

from src.main.shared.database.main import get_db
from src.main.shared.jwt_util import get_access_token_preferred_username, get_access_token_oid
from src.main.user.settings import settings
from src.main.user.util import assert_is_username_and_email_not_taken, assert_is_user_exists, \
    emit_user_registered_event, emit_user_deleted_event
from random_username.generate import generate_username
from src.main.user import crud

router = APIRouter(prefix=settings.SERVICE_PREFIX)


@router.get("/registered", status_code=HTTP_200_OK)
def check_if_registered(request: Request, db: Session = Depends(get_db)):
    email = get_access_token_preferred_username(request)
    registered = crud.get_user_by_email(db=db, email=email) is not None

    return {"registered": registered}


@router.get("/username", status_code=HTTP_200_OK)
def get_username(request: Request, db: Session = Depends(get_db)):
    email = get_access_token_preferred_username(request)
    user = crud.get_user_by_email(db=db, email=email)
    assert_is_user_exists(user)

    return {"username": user.username}


@router.post("", status_code=HTTP_201_CREATED)
async def create_user(request: Request, background_tasks: BackgroundTasks,
                      db: Session = Depends(get_db)):
    email = get_access_token_preferred_username(request)
    new_username = generate_username(1)[0]

    # It might happen that the randomly generated username is already taken.
    is_username_taken = crud.get_user_by_username(db=db, username=new_username) is not None
    while is_username_taken:
        new_username = generate_username(1)[0]
        is_username_taken = crud.get_user_by_username(db=db, username=new_username) is not None

    assert_is_username_and_email_not_taken(username=new_username, email=email, db=db)

    crud.create_user(db=db, username=new_username, email=email)

    oid = get_access_token_oid(request)
    background_tasks.add_task(emit_user_registered_event, request=request, email=email, oid=oid,
                              username=new_username)

    return


@router.delete("", status_code=HTTP_204_NO_CONTENT)
def delete_user(request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    email = get_access_token_preferred_username(request)
    user = crud.get_user_by_email(db=db, email=email)
    assert_is_user_exists(user)

    crud.delete_user(db=db, email=email)

    oid = get_access_token_oid(request)
    background_tasks.add_task(emit_user_deleted_event, request=request, oid=oid)

    return
