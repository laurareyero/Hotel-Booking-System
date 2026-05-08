from typing import Optional
from pydantic import BaseModel


class Guest(BaseModel):
    id_guest: Optional[int] = None
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: str
    dni: str

    class Config:
        from_attributes = True


class Room(BaseModel):
    id_room: Optional[int] = None
    room_number: int
    room_type: str          # single / double / suite
    price_per_night: float
    status: Optional[str] = "available"   # available / occupied

    class Config:
        from_attributes = True


class Booking(BaseModel):
    id_booking: Optional[int] = None
    id_guest: int
    id_room: int
    check_in_date: str
    check_out_date: str
    total_price: float
    status: Optional[str] = "pending"    # pending / confirmed / canceled

    class Config:
        from_attributes = True
