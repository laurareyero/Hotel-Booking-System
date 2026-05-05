# 🏨 Hotel Booking System

> **Python from Zero to Hero · Final Project 2025–2026**  
> A full-stack hotel management platform built with PostgreSQL · FastAPI · Streamlit

---

## 👥 Team

| Role | Name |
|------|------|
| Speaker | _(add name)_ |
| Member | _(add name)_ |
| Member | _(add name)_ |
| Member | _(add name)_ |

---

## 📁 Project Structure

```
hotel-booking-system/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── routes/
│   │   ├── people.py
│   │   └── reservations.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── database/
│   └── schema.sql
│
├── .gitignore
└── README.md
```

---

## ✅ To-Do List

### 🗄️ Database — `database/schema.sql`

- [ ] Create `personas` table with fields: `id`, `nombre`, `apellidos`, `email`, `telefono`, `dni`, `nacionalidad`, `fecha_nacimiento`, `created_at`, `updated_at`
- [ ] Create `reservations` table with fields: `id`, `persona_id` (FK), `room_id`, `fecha_entrada`, `fecha_salida`, `num_huespedes`, `estado`, `precio_total`, `notas`, `created_at`, `updated_at`
- [ ] Add foreign key constraint linking `reservations.persona_id` → `personas.id`
- [ ] Add `CHECK` constraint to ensure `fecha_salida > fecha_entrada`
- [ ] Add `CHECK` constraint for valid `estado` values (`confirmada`, `pendiente`, `cancelada`, `completada`)
- [ ] Add `updated_at` auto-update trigger
- [ ] Insert seed/sample data for testing
- [ ] Run schema against local PostgreSQL and verify tables are created correctly

---

### ⚙️ Backend — `backend/`

#### `database.py`
- [ ] Configure `psycopg` connection using environment variables (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`)
- [ ] Create a `get_connection()` helper / dependency

#### `models.py`
- [ ] Define Pydantic model `PersonaBase` (shared fields)
- [ ] Define `PersonaCreate` (input — inherits `PersonaBase`)
- [ ] Define `PersonaResponse` (output — adds `id`, `created_at`)
- [ ] Define Pydantic model `ReservationBase` (shared fields)
- [ ] Define `ReservationCreate` (input)
- [ ] Define `ReservationResponse` (output — adds `id`, `created_at`)

#### `routes/people.py`
- [ ] `GET /personas` — list all guests
- [ ] `GET /personas/{id}` — get one guest by ID
- [ ] `POST /personas` — create a new guest
- [ ] `PUT /personas/{id}` — update guest data
- [ ] `DELETE /personas/{id}` — delete a guest

#### `routes/reservations.py`
- [ ] `GET /reservations` — list all reservations (optionally filter by `estado`)
- [ ] `GET /reservations/{id}` — get one reservation by ID
- [ ] `POST /reservations` — create a new reservation
- [ ] `PUT /reservations/{id}` — update a reservation
- [ ] `DELETE /reservations/{id}` — cancel/delete a reservation

#### `main.py`
- [ ] Initialise `FastAPI` app with title and description
- [ ] Register routers for `/personas` and `/reservations`
- [ ] Add CORS middleware (required for Streamlit → FastAPI communication)
- [ ] Add root health-check endpoint `GET /`

#### `backend/requirements.txt`
- [ ] Add `fastapi`
- [ ] Add `uvicorn[standard]`
- [ ] Add `psycopg[binary]`
- [ ] Add `pydantic`
- [ ] Add `python-dotenv`

---

### 🖥️ Frontend — `frontend/`

#### `app.py`
- [ ] Configure `BASE_URL` pointing to FastAPI (`http://localhost:8000`)
- [ ] Build sidebar navigation (Reservations / Guests / New Booking / New Guest)

**Reservations view**
- [ ] Fetch and display all reservations in a table (`GET /reservations`)
- [ ] Add status filter widget (All / Confirmada / Pendiente / Cancelada)
- [ ] Add "Modify reservation" form (loads existing data → `PUT /reservations/{id}`)
- [ ] Add "Cancel reservation" button → `DELETE /reservations/{id}`

**Guests view**
- [ ] Fetch and display all registered guests (`GET /personas`)
- [ ] Add search/filter by name or DNI
- [ ] Add "Edit guest" form → `PUT /personas/{id}`
- [ ] Add "Delete guest" button → `DELETE /personas/{id}`

**New Booking form**
- [ ] Guest selector (dropdown from `GET /personas`)
- [ ] Date pickers for `fecha_entrada` / `fecha_salida`
- [ ] Number of guests input
- [ ] Room selector + status selector
- [ ] Submit → `POST /reservations`

**New Guest form**
- [ ] Input fields: nombre, apellidos, email, teléfono, DNI, nacionalidad, fecha de nacimiento
- [ ] Submit → `POST /personas`

#### `frontend/requirements.txt`
- [ ] Add `streamlit`
- [ ] Add `requests`
- [ ] Add `pandas`

---

### 🔧 Configuration & DevOps

- [ ] Create `.env` file with DB credentials (do **not** commit to Git)
- [ ] Add `.env` to `.gitignore`
- [ ] Add `__pycache__/`, `*.pyc`, `.DS_Store` to `.gitignore`
- [ ] Test full flow locally: PostgreSQL → FastAPI → Streamlit
- [ ] Verify all CRUD operations work end-to-end from the UI

---

### 🎤 Presentation

- [ ] Assign presenter (speaker)
- [ ] Send team member list + speaker name to the teacher
- [ ] Prepare a live demo walkthrough:
  - [ ] Create a guest
  - [ ] Create a reservation for that guest
  - [ ] Modify the reservation
  - [ ] Cancel the reservation
- [ ] Be ready to explain the database schema and API design choices

---

## 🚀 How to Run

### 1. Database
```bash
psql -U postgres -d hotel_db -f database/schema.sql
```

### 2. Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# API docs available at http://localhost:8000/docs
```

### 3. Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Database | PostgreSQL + psycopg |
| Backend | FastAPI + Uvicorn |
| Data Validation | Pydantic |
| Frontend | Streamlit |
