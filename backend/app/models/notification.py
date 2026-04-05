from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database.connection import Base
from datetime import datetime

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    subject = Column(String)
    sender = Column(String)
    action = Column(String)

    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)