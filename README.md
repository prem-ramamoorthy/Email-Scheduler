# 🔔 Email Scheduler (SaaS) with FastAPI

A backend-only SaaS application built with **FastAPI** that allows users to schedule emails with token-based authentication and email sending limits based on subscription plans.

---

## ✨ Features

- 🧪 **User Registration & Login** with UUID token
- 📬 **Email Scheduling** with APScheduler
- ⏰ Supports scheduling emails for future delivery
- 🔐 **Token-based Authentication** for API access
- 📦 Configurable **Email Limits** per user
- 📫 Sends emails via SMTP (Gmail)
- 🗃️ Lightweight with SQLite (or switch to PostgreSQL)

---

## 📦 Tech Stack

- Backend: **FastAPI**
- Scheduling: **APScheduler**
- Emailing: **smtplib**
- Auth: **UUID token**
- Database: **SQLite** (easy to swap with Postgres)

---

## 🚀 Endpoints

### Register a new user
```http
POST /register
```
Returns a unique token for authentication.

### Schedule an email
```http
POST /schedule
Headers:
  token: <your_token>
Body (JSON):
{
  "to_email": "example@example.com",
  "subject": "Test Email",
  "body": "This is a test message",
  "send_at": "2025-04-06T17:30:00"
}
```

---

## 🔧 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/email-scheduler.git
cd email-scheduler
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn main:app --reload
```

---

## 🛡️ Note on Security
Make sure to store your email credentials securely using environment variables or a secret manager.

---

## 📫 Contact
For queries or suggestions, reach out at **pkpf321@gmail.com**

