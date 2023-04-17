from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.post import crud, model
from src.main.post.schema import Post as PostSchema
from src.main.post.schema import PostCreate as PostCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=list[PostSchema])
def get_10_posts(request: Request, page: int = 0, db: Session = Depends(get_db)):
    # print(request.headers['authorization']) # TODO: use jwt to extract username etc..
    return crud.get_10_posts(db=db, page=page)


@app.get("/{post_id}", response_model=PostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(db=db, post_id=post_id)


@app.post("/", status_code=201, response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@app.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db=db, post_id=post_id)
