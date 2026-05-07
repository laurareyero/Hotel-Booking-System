import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


class Person(BaseModel):
    id_person: int
    first_name: str
    last_name:  str
    email: str | None = None
    phone: str
    dni: str

    class Config:
        from_attributes = True


class Room(BaseModel):
    id_room: int
    room_number: int
    room_type: str #single / double / suite
    price_per_night: float
    status: str | None = "available"  # available / occupied

    class Config:
        from_attributes = True


class Booking(BaseModel):
    id_booking: int
    id_person: int    #foreign key: Person
    id_room: int  #foreign key: Room
    check_in_date: str
    check_out_date: str
    total_price: float
    status: str | None = "pending" # pending / confirmed / canceled

    class Config:
        from_attributes = True
