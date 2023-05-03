from sqlalchemy.orm import Session

from src.main.vote.model import Vote as VoteModel


def cast_vote(db: Session, vote: dict):
    db_vote = VoteModel(**vote)
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return
