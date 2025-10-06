# FastAPI User Management API

This project is a **complete user management API** built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It provides all essential operations to manage users, including creating, reading, updating, and deleting (CRUD) users, with input validation and database version control.  

The project is modular, maintainable, and easy to extend for future features like authentication, role-based access, or reporting.

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation & Setup](#installation--setup)  
4. [Database Migrations](#database-migrations)  
5. [Running the Application](#running-the-application)  
6. [Project Structure](#project-structure)  
7. [API Endpoints](#api-endpoints)  
8. [Database Schema](#database-schema)  
9. [How the Code Works](#how-the-code-works)   

---

## Features

- **CRUD operations**: Create, Read, Update, Delete users via API endpoints.  
- **Database versioning with Alembic**: Manage schema changes safely.  
- **PostgreSQL integration**: Production-ready relational database.  
- **Input validation**: Pydantic schemas validate data before hitting DB.  
- **Filtering & Pagination**: Retrieve lists of users with optional filtering.  
- **Modular architecture**: Separate files for database, models, schemas, and CRUD.  
- **Interactive API documentation**: Swagger UI and ReDoc.

---

## Prerequisites

- **Python 3.8+**  
- **PostgreSQL**  
- **pgAdmin 4** (optional)  
- **pip**  
- **git**

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-user-management.git
cd fastapi-user-management
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate:

```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Packages include `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, `pydantic`, `python-dotenv`.

### 4. Set up PostgreSQL database

```sql
CREATE DATABASE user_management;
```

Update `.env` or `database.py`:

```
DATABASE_URL=postgresql://username:password@localhost:5432/user_management
```

---

## Database Migrations

```bash
# Apply all migrations
alembic upgrade head

# Rollback one step if needed
alembic downgrade -1
```

Alembic allows version control of the DB schema without losing data.

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

* Available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
* `--reload` automatically reloads server on code changes.

### API Documentation

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Project Structure

```text
fastapi-user-management/
│
├── app/
│   ├── main.py          # FastAPI app & routes
│   ├── database.py      # DB connection and session
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD functions
│   └── routers/
│       └── users.py     # User-specific routes
│
├── alembic/             # DB migrations
├── requirements.txt     # Python dependencies
└── README.md
```

---

## API Endpoints

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| GET    | `/`           | Welcome / health check          |
| POST   | `/users`      | Create a new user               |
| GET    | `/users`      | List users (optional filtering) |
| GET    | `/users/{id}` | Retrieve user by ID             |
| PUT    | `/users/{id}` | Update an existing user         |
| DELETE | `/users/{id}` | Delete a user by ID             |

**Example request (create user):**

```json
POST /users
{
  "name": "Alice",
  "email": "alice@example.com",
  "phone_number": "1234567890",
  "address": "123 Main St"
}
```

**Example response:**

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "phone_number": "1234567890",
  "address": "123 Main St",
  "created_at": "2025-10-06T10:00:00"
}
```

---

## Database Schema

**Users Table:**

| Column       | Type     | Notes                         |
| ------------ | -------- | ----------------------------- |
| id           | Integer  | Primary Key, auto-incremented |
| name         | String   | Required                      |
| email        | String   | Required, Unique              |
| created_at   | DateTime | Default = now()               |
| phone_number | String   | Optional (nullable)           |
| address      | String   | Optional (nullable)           |

---

## How the Code Works

1. **Database connection (`database.py`)**: Engine + session factory.
2. **Models (`models.py`)**: SQLAlchemy ORM tables.
3. **Schemas (`schemas.py`)**: Pydantic models for validation/serialization.
4. **CRUD operations (`crud.py`)**: Functions for DB operations.
5. **Routes (`users.py`)**: API endpoints calling CRUD functions.

---
