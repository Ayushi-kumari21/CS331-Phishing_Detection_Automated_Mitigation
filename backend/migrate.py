# run this once as: python migrate.py
import sqlite3
from app.database.connection import engine, Base

from app.models.user import User
from app.models.email import Email
from app.models.notification import Notification

# CREATE TABLES (NEW)

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

conn = sqlite3.connect("sentinelphish.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE users ADD COLUMN gmail_token TEXT")
    print("Added gmail_token")
except:
    print("gmail_token already exists")

try:
    cursor.execute("ALTER TABLE users ADD COLUMN gmail_connected BOOLEAN DEFAULT 0")
    print("Added gmail_connected")
except:
    print("gmail_connected already exists")

conn.commit()
conn.close()
print("Migration completed!")

