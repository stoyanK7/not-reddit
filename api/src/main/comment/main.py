from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.main.shared.database.main import get_db, engine
from src.main.comment import crud, model
from src.main.comment.schema import Comment as CommentSchema, CommentCreate as CommentCreateSchema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", response_model=list[CommentSchema])
def get_10_comments(page: int = 0, db: Session = Depends(get_db)):
    return crud.get_10_comments(db=db, page=page)


@app.post("/", status_code=201, response_model=CommentSchema)
def create_comment(comment: CommentCreateSchema, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)


@app.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    return crud.delete_comment(db=db, comment_id=comment_id)
