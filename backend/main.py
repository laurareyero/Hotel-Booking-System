from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import guests, rooms, bookings

app = FastAPI(title="Hotel Booking API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guests.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
