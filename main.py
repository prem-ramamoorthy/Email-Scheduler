from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import Base, engine
from auth import create_user, get_current_user, get_db
from models import Email
from datetime import datetime
import scheduler

app = FastAPI()
Base.metadata.create_all(bind=engine)

class RegisterRequest(BaseModel):
    username: str
    password: str
    plan: str  # Free or Pro

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str
    send_at: datetime

@app.get("/")
def start():
    return {"detail" : "App started"}

@app.post("/register")
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    return {"token": create_user(req.username, req.password, req.plan, db)}

@app.post("/schedule")
def schedule_email(req: EmailRequest, user=Depends(get_current_user), db: Session = Depends(get_db)):
    # Quota check
    today = datetime.utcnow().date()
    daily_limit = 10 if user.plan == "Free" else 100

    sent_today = db.query(Email).filter(
        Email.user_id == user.id,
        Email.send_at >= datetime(today.year, today.month, today.day),
        Email.send_at < datetime(today.year, today.month, today.day + 1)
    ).count()

    if sent_today >= daily_limit:
        return {"error": "Daily email limit reached"}

    email = Email(
        to_email=req.to_email,
        subject=req.subject,
        body=req.body,
        send_at=req.send_at,
        owner=user
    )
    db.add(email)
    db.commit()
    return {"message": "Email scheduled"}