from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    plan = Column(String, default="Free")  # Free or Pro
    token = Column(String, unique=True)

    emails = relationship("Email", back_populates="owner")

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    to_email = Column(String)
    subject = Column(String)
    body = Column(String)
    send_at = Column(DateTime)
    sent = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="emails")
