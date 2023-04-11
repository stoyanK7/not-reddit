from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.database import get_db, engine
from src.main.comment import crud, model
from src.main.comment.schema import Comment as CommentSchema, CommentCreate as CommentCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter(prefix="/comment")


@router.get("/", response_model=list[CommentSchema])
def get_10_comments(page: int = 0, db: Session = Depends(get_db)):
    return crud.get_10_comments(db=db, page=page)


@router.post("/", status_code=201, response_model=CommentSchema)
def create_comment(comment: CommentCreateSchema, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)


@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return crud.delete_comment(db=db, comment_id=comment_id)


app.include_router(router)
