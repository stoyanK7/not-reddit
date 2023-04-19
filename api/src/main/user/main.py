import jwt
from fastapi import FastAPI, Depends, HTTPException, Request
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user import crud, model
from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered
from src.main.auth_config import configure_cors, azure_scheme

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.post("/", status_code=HTTP_201_CREATED, dependencies=[Depends(azure_scheme)])
def create_user(request: Request, body: UserCreate, db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)
    assert_is_username_and_email_not_taken(body.username, body.email, db=db)

    crud.create_user(db=db, user=body)
    return


@app.get("/{username}", status_code=HTTP_200_OK, dependencies=[Depends(azure_scheme)])
def get_user(username: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, username=username)


@app.post("/registered", status_code=HTTP_200_OK, dependencies=[Depends(azure_scheme)])
def check_if_registered(request: Request, body: UserCheckIfRegistered,
                        db: Session = Depends(get_db)):
    assert_is_jwt_email_same_as_provided_email(body.email, request=request)

    registered = crud.get_user_by_email(db=db, email=body.email) is not None
    return {"registered": registered}


def assert_is_jwt_email_same_as_provided_email(provided_email: str, request: Request):
    jwt_token = extract_token(request.headers['Authorization'])
    decoded = jwt.decode(jwt_token, options={"verify_signature": False})
    is_jwt_email_same_as_body_email = decoded['preferred_username'] == provided_email

    if not is_jwt_email_same_as_body_email:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )


def assert_is_username_and_email_not_taken(username: str, email: str, db: Session):
    is_username_or_email_taken = crud.get_user_by_username_or_email(db=db, username=username,
                                                                    email=email)
    if is_username_or_email_taken:
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="Username or email already taken"
        )


def extract_token(authorization_header: str):
    """Extracts the token from the authorization header by removing the 'Bearer ' part."""
    return authorization_header[7:]
