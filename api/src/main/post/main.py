from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session

from src.main.database import get_db, engine
from src.main.post import crud, model
from src.main.post.schema import Post as PostSchema
from src.main.post.schema import PostCreate as PostCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter(prefix="/post")


@router.get("/", response_model=list[PostSchema])
def get_posts(page: int = 0, db: Session = Depends(get_db)):
    return crud.get_10_posts(db=db, page=page)


@router.get("/{post_id}", response_model=PostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(db=db, post_id=post_id)


@router.post("/", status_code=201, response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db=db, post_id=post_id)


app.include_router(router)
