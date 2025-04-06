import uuid
from passlib.hash import bcrypt
from fastapi import HTTPException, Depends, Header
from sqlalchemy.orm import Session
from database import SessionLocal
import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(username: str, password: str, plan: str, db: Session):
    hashed_pw = bcrypt.hash(password)
    token = str(uuid.uuid4())
    user = models.User(username=username, password=hashed_pw, plan=plan, token=token)
    db.add(user)
    db.commit()
    db.refresh(user)
    return token

def get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
