from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.dal.notification_dal import (
    get_all_notifications,
    get_unread_count,
    mark_notification_as_read
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])


# 🔧 DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET ALL NOTIFICATIONS
@router.get("/")
def fetch_notifications(db: Session = Depends(get_db)):
    notifications = get_all_notifications(db)

    return [
        {
            "id": n.id,
            "subject": n.subject,
            "sender": n.sender,
            "action": n.action,
            "is_read": n.is_read,
            "created_at": n.created_at
        }
        for n in notifications
    ]


# ✅ GET UNREAD COUNT
@router.get("/unread")
def unread_notifications(db: Session = Depends(get_db)):
    count = get_unread_count(db)
    return {"count": count}


# ✅ MARK AS READ
@router.post("/read/{notification_id}")
def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    mark_notification_as_read(db, notification_id)
    return {"message": "Notification marked as read"}