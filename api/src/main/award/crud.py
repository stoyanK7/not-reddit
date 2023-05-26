from sqlalchemy.orm import Session

from src.main.award.model import Award as AwardModel


def create_award(db: Session, payment_intent: str, award_type: str, subject_type: str,
                 subject_id: int, paid: bool = False):
    db_award = AwardModel(payment_intent=payment_intent, award_type=award_type,
                          subject_type=subject_type, subject_id=subject_id, paid=paid)
    db.add(db_award)
    db.commit()
    db.refresh(db_award)


def get_award_by_payment_intent(db: Session, payment_intent: str):
    return db.query(AwardModel).filter(AwardModel.payment_intent == payment_intent).first()


def set_award_to_paid(db: Session, award: AwardModel):
    award.paid = True
    db.commit()
    db.refresh(award)
