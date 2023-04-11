from sqlalchemy.orm import Session
from .schema import VoteCreate
from .model import Vote as VoteModel


def cast_vote(db: Session, vote: VoteCreate):
    db_vote = VoteModel(**vote.dict())
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return
