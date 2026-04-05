from app.models.notification import Notification
from datetime import datetime


# 🔥 MODIFIED: Create notification (structured)
def create_notification(db, subject, sender, action):
    notification = Notification(
        subject=subject,
        sender=sender,
        action=action,
        is_read=False,
        created_at=datetime.utcnow()
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification


# ✅ Get all notifications (no change)
def get_all_notifications(db):
    return db.query(Notification).order_by(Notification.created_at.desc()).all()


# ✅ Get unread count (no change)
def get_unread_count(db):
    return db.query(Notification).filter(Notification.is_read == False).count()


# ✅ Mark notification as read (no change)
def mark_notification_as_read(db, notification_id):
    notif = db.query(Notification).filter(Notification.id == notification_id).first()
    if notif:
        notif.is_read = True
        db.commit()
        return notif
    return None