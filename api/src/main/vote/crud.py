from sqlalchemy.orm import Session

from src.main.vote.schema import VoteCreate
from src.main.vote.model import Vote as VoteModel


def cast_vote(db: Session, vote: VoteCreate):
    db_vote = VoteModel(**vote.dict())
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return
