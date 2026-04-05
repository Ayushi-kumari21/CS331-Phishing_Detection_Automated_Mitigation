from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.connection import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)

    gmail_id = Column(String, unique=True, index=True)  # unique Gmail message ID

    subject = Column(String)
    sender = Column(String)

    category = Column(String)        # Safe / Suspicious / Phishing
    risk_score = Column(Float)

    action_taken = Column(String)    # moved_to_spam / none

    scanned_at = Column(DateTime, default=datetime.utcnow)