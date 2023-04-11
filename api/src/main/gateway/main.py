from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from src.main.database import get_db
from src.main.gateway.auth import create_access_token, authenticate_user
from src.main.gateway.schema import Token
from src.main.gateway.routers.user import router as user_router
from src.main.gateway.routers.comment import router as comment_router
from src.main.gateway.routers.post import router as post_router
from src.main.gateway.routers.subreddit import router as subreddit_router
from src.main.gateway.routers.vote import router as vote_router

app = FastAPI()


@app.post("/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(subreddit_router)
app.include_router(vote_router)
