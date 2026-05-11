from typing import Optional
from pydantic import BaseModel


class Guest(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: str
    dni: str

    class Config:
        from_attributes = True

class Room(BaseModel):
    id: Optional[int] = None
    number: int
    type: str
    base_price: float
    capacity: Optional[int] = None
    description: Optional[str] = None
    available: Optional[bool] = True


    class Config:
        from_attributes = True


class Booking(BaseModel):
    id: Optional[int] = None
    guest_id: int
    room_id: int
    check_in: str
    check_out: str
    status: Optional[str] = "pending"
    total_price: float
    info_adicional:str
    

    class Config:
        from_attributes = True
