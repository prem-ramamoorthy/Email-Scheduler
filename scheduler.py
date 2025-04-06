from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from datetime import datetime
from database import SessionLocal
from models import Email
from email_utils import send_email

def job():
    db: Session = SessionLocal()
    now = datetime.utcnow()
    emails = db.query(Email).filter(Email.send_at <= now, Email.sent == False).all()
    for email in emails:
        send_email(email.to_email, email.subject, email.body)
        email.sent = True
    db.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=60)
scheduler.start()
