from fastapi import FastAPI
from routes import guests, rooms, bookings
 
app = FastAPI(title="Hotel Booking API")
 
app.include_router(guests.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
 