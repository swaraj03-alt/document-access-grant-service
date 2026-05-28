# Document Access Grant Service

Backend service for managing temporary document sharing grants.

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Docker
* Pytest
* Async SQLAlchemy

---

# Features

* Create temporary document access grants
* Prevent duplicate active grants
* Revoke grants
* Check grant active status
* PostgreSQL schema management
* Alembic migrations
* Dockerized PostgreSQL
* Async database operations
* Automated API tests

---

# Project Structure

```text
document-access-grant-service/
│
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── alembic/
├── tests/
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd document-access-grant-service
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

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

## 4. Start PostgreSQL with Docker

```bash
docker compose up -d
```

---

## 5. Run Database Migrations

```bash
alembic upgrade head
```

---

## 6. Seed Initial Data

```bash
python -m app.seed
```

---

## 7. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Create Grant

```http
POST /grants
```

Creates a new temporary document access grant.

---

## List Grants

```http
GET /grants
```

Returns all grants.

---

## Get Grant By ID

```http
GET /grants/{grant_id}
```

Returns a specific grant.

---

## Revoke Grant

```http
DELETE /grants/{grant_id}
```

Revokes an active grant.

---

## Check Grant Status

```http
GET /grants/{grant_id}/check
```

Checks whether a grant is currently active.

---

# Business Rules

* Grant expiry must be at least 1 minute in the future
* Duplicate active grants are not allowed
* Revoked grants become inactive immediately
* Expired grants are automatically treated as inactive

---

# Database

## PostgreSQL Schema

```text
grants_svc
```

## Tables

* users
* documents
* grants

---

# Seeded Data

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
* Database Layer → SQLAlchemy ORM
* Persistence Layer → PostgreSQL

This separation improves maintainability, scalability, and testability.

---

# Author

Backend Take-Home Assignment Submission
