from sqlalchemy import Column, String, Integer, Boolean

from src.main.shared.database.main import Base


class Award(Base):
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True, index=True)
    award_type = Column(String)
    subject_type = Column(String)
    subject_id = Column(Integer)
    payment_intent = Column(String, unique=True)
    paid = Column(Boolean, default=False)
