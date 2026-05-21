# Paquito Hotel — Booking Management System

> Final project for **Python From Zero to Hero 2025-2026**

A full-stack hotel management platform built with **FastAPI**, **PostgreSQL**, and **Streamlit**. Designed for hotel administrators to manage guests, rooms, and reservations from a single, intuitive dashboard.

---

## Architecture

The system is composed of three independent layers that communicate over HTTP and are orchestrated with Docker Compose:

- **Frontend (Streamlit):** A multi-page dashboard that calls the API using the `requests` library. It never touches the database directly.
- **Backend (FastAPI):** A RESTful API that handles all business logic, validates data with Pydantic, and communicates with the database asynchronously.
- **Database (PostgreSQL):** A hosted Supabase PostgreSQL instance with three related tables.

The data flows in one direction: Streamlit → FastAPI → PostgreSQL. Each layer is completely independent and runs in its own Docker container.

---

## Project Structure

```
Hotel-Booking-System/
├── backend/
│   ├── dao/                    # Data Access Layer (one class per entity)
│   ├── routes/                 # API endpoints (one file per entity)
│   ├── database.py             # Async DB connection manager
│   ├── models.py               # Pydantic data models
│   ├── exceptions.py           # Custom exception hierarchy
│   ├── decorators.py           # @auditoria_endpoint logging decorator
│   ├── main.py                 # FastAPI app entry point + CORS
│   └── Dockerfile
├── frontend/
│   ├── .streamlit/
│   │   └── config.toml         # Custom warm luxury theme
│   ├── pages/                  # One page per entity
│   ├── src/
│   │   ├── api_client.py       # All HTTP calls to the API
│   │   └── sidebar.py          # Shared sidebar component
│   ├── Hotel_App.py            # Main dashboard (metrics overview)
│   └── Dockerfile
├── database/
│   └── schema.sql              # PostgreSQL schema
├── docker-compose.yml
├── .env                        # Environment variables (not in Git)
└── .gitignore
```

---

## Step 1 — Database Design

The database has three tables with proper normalization and referential integrity.

**guests** stores all hotel guest information: first name, last name, email, phone, and DNI. Both the email and DNI fields are unique, which prevents duplicate guest records at the database level.

**rooms** stores the hotel room inventory: room number, type (single, double, suite, or deluxe), price per night, and availability status. The room number is also unique — no two rooms can share the same number.

**bookings** is the central table that links guests to rooms. It stores the check-in and check-out dates, the total price, and the reservation status (pending, confirmed, cancelled, or completed). It references both the guests and rooms tables with foreign keys and cascading deletes. A database-level constraint also enforces that the check-out date must always be after the check-in date.

---

## Step 2 — Pydantic Models

Each of the three entities has a Pydantic model that defines the expected data structure. FastAPI uses these models to automatically validate every incoming request — if a required field is missing or has the wrong type, the API returns a `422 Unprocessable Entity` error before any database call is made.

The models also handle optional fields gracefully. For example, `id_guest` is optional on creation (the database assigns it automatically) but required on updates.

---

## Step 3 — Async Database Connection

All database operations use `psycopg.AsyncConnection`, making the entire backend non-blocking. This means that while the backend is waiting for the database to respond, FastAPI can continue serving other incoming requests concurrently — a significant performance advantage over synchronous connections.

The connection manager is built as an async context manager. It opens a connection, runs the query, commits the transaction, and closes the connection automatically. It also intercepts specific PostgreSQL errors — such as unique constraint violations, foreign key violations, and null value violations — and converts them into meaningful HTTP responses instead of letting them bubble up as generic 500 errors.

---

## Step 4 — Data Access Layer (DAO Pattern)

Each entity has its own DAO class (`GuestDAO`, `RoomDAO`, `BookingDAO`) that encapsulates all SQL queries. The routes never write SQL directly — they only call DAO methods. This separation of concerns makes the code easier to maintain and test.

Every DAO method is asynchronous and follows the same pattern: open an async connection, execute the query, fetch the results, and return them as Pydantic model instances.

---

## Step 5 — Custom Exception Hierarchy

Instead of scattering generic HTTP exceptions throughout the code, the project uses a clean exception hierarchy rooted in a base `HotelError` class. Each specific error — such as `GuestNotFoundError`, `RoomNotAvailableError`, or `InvalidStatusError` — knows its own HTTP status code and error message.

This approach keeps the route code clean and readable. A route simply raises the appropriate domain exception, which converts itself into a FastAPI HTTP response. It also makes error handling consistent across the entire API.

---

## Step 6 — Audit Decorator

Every single endpoint in the API is decorated with `@auditoria_endpoint`. This decorator wraps each route function and automatically logs three things: when the endpoint was called and with what parameters, when it completed successfully, and if it failed — what the error was.

This means full request tracing is achieved without adding any logging code inside the route functions themselves. All logs are visible in the Docker container output during runtime.

---

## Step 7 — API Endpoints

The API exposes full CRUD operations for all three entities, plus a dedicated PATCH endpoint to update booking status independently.

**Guests:** list all, get by ID, create, update, delete.

**Rooms:** list all, get by ID, create, update, delete.

**Bookings:** list all, get by ID, create, update, delete, and update status only (PATCH).

All endpoints are documented automatically by FastAPI and can be tested interactively at `http://localhost:8000/docs`.

---

## Step 8 — Room Status Automation

The booking system automatically keeps room availability in sync with reservations. When a booking is created, the room is immediately marked as occupied. When a booking is deleted, the room is freed back to available. When the status is changed via the PATCH endpoint, the room status updates accordingly — but only marks the room as available again if there are no other active confirmed bookings for that room.

---

## Step 9 — Streamlit Frontend

The frontend is a multi-page Streamlit application with a custom warm luxury theme inspired by a Mediterranean hotel — deep warm browns for the background, gold as the primary colour, and cream for the text.

The main dashboard shows real-time metrics for total guests, rooms, and bookings, as well as a breakdown of booking statuses. Each of the three management pages (Guests, Rooms, Bookings) provides a visual card overview followed by full CRUD forms.

Notable UX features include automatic total price calculation based on the number of nights and the room's price per night, date validation that prevents check-out before check-in, and colour-coded status indicators for both rooms and bookings.

The frontend communicates with the backend exclusively through `api_client.py`, which centralises all HTTP calls and reads the API base URL from an environment variable — making it easy to switch between local development and production.

---

## Step 10 — Security

Database credentials are never stored in the source code. They live in a `.env` file in the project root, which is listed in `.gitignore` and never committed to the repository. Docker Compose reads the `.env` file at startup and injects the `DATABASE_URL` as an environment variable into the backend container. Anyone cloning the repository must create their own `.env` file with their own credentials.

---



### Prerequisites
Docker and Docker Compose installed on your machine.

### 1. Clone the repository
```
git clone https://github.com/your-username/Hotel-Booking-System.git
cd Hotel-Booking-System
```

### 2. Create the `.env` file in the project root
```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### 3. Run with Docker Compose
```
docker-compose up --build
```

### 4. Open the app

| Service | URL |
|---------|-----|
| Streamlit Frontend | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| Swagger API Docs | http://localhost:8000/docs |

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Interactive admin dashboard |
| Backend | FastAPI + Uvicorn | Async REST API |
| Database | PostgreSQL (Supabase) | Persistent storage |
| DB Driver | psycopg3 (async) | Non-blocking DB connections |
| Validation | Pydantic | Data models and request validation |
| Containerization | Docker + Docker Compose | Deployment and orchestration |

---

## Group

| Name | Role |
|------|------|
| Sofía González ||
| Laura Jiménez ||
| Laura reyero | Speaker |

