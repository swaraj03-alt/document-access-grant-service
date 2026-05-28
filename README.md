# Document Access Grant Service

Async backend service for managing temporary document access grants using FastAPI and PostgreSQL.

---

# Tech Stack

* Python 3.13
* FastAPI
* PostgreSQL
* SQLAlchemy 2.0 (async)
* asyncpg
* Alembic
* Pydantic v2
* Docker
* Pytest
* pytest-asyncio

---

# Features

* Create temporary document access grants
* Prevent duplicate active grants
* Revoke grants
* Check active grant status
* Async PostgreSQL integration
* Alembic migration support
* Dockerized PostgreSQL setup
* Deterministic seed data
* Automated API testing
* Layered backend architecture

---

# Business Rules Implemented

* Expiry must be at least 1 minute in the future
* Only one active grant per grantee/document pair
* Only creator can revoke grants
* Cannot revoke expired or already revoked grants
* Inactive grants remain permanently stored

---

# Project Structure

```text
document-access-grant-service/
│
├── alembic/
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── README.md
└── SOLUTION.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/swaraj03-alt/document-access-grant-service.git
cd document-access-grant-service
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.\.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start PostgreSQL

```bash
docker compose up -d
```

---

## 5. Run Alembic Migrations

```bash
alembic upgrade head
```

---

## 6. Seed Database

```bash
python -m app.seed
```

---

## 7. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint                 | Description               |
| ------ | ------------------------ | ------------------------- |
| POST   | /grants                  | Create grant              |
| GET    | /grants                  | List grants               |
| GET    | /grants/{grant_id}       | Get single grant          |
| DELETE | /grants/{grant_id}       | Revoke grant              |
| GET    | /grants/{grant_id}/check | Check grant active status |

---

# PostgreSQL Schema

```text
grants_svc
```

## Tables

* users
* documents
* grants

---

# Seed Data

## Users

* Alice
* Bob
* Carol

## Documents

* Q1 Report
* Product Roadmap
* Budget 2026

---

# Running Tests

```bash
pytest
```

---

# Architecture

The application follows a layered backend architecture:

* API Layer → FastAPI routes
* Service Layer → business logic
* ORM Layer → SQLAlchemy async models
* Persistence Layer → PostgreSQL database

This separation improves maintainability, scalability, and testability.

---

# Assignment Completion Checklist

* FastAPI backend implemented
* PostgreSQL + Docker setup completed
* Alembic migrations included
* Async SQLAlchemy integration completed
* Business validation rules implemented
* REST endpoints completed
* Seed data added
* Automated tests added
* README and SOLUTION documentation included

---

# Repository

https://github.com/swaraj03-alt/document-access-grant-service
