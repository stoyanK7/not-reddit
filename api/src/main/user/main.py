from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.user import crud, model
from src.main.user.schema import UserCreate
from src.main.user.schema import UserCheckIfRegistered
from src.main.auth_config import configure_cors, azure_scheme

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
configure_cors(app)


@app.post("/", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # TODO: check token an ensure email is the same as the one in the token
    # TODO: check if username and email are unique
    crud.create_user(db=db, user=user)
    return


@app.get("/{username}", status_code=200, dependencies=[Depends(azure_scheme)])
def get_user(username: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, username=username)


@app.post("/registered", status_code=200)
def check_if_registered(request: Request, body: UserCheckIfRegistered,
                        db: Session = Depends(get_db)):
    # TODO: check if request is made by the same user
    print(request.headers)
    print('hello')
    registered = crud.check_if_registered(db=db, email=body.email)
    return {"registered": registered}
