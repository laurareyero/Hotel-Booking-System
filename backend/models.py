import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


class Persona(BaseModel):
    id_person: int
    name: str
    lastname: str
    email: str | None = None
    age: int

    class Config:
        from_attributes = True 

class Reservation(BaseModel):
    id_reservation: int
    id_person: int # foreign key - Persona
    room_number: int
    check_in_date: str
    check_out_date: str          
    price_per_night: float
    status: str | None = "pending" # pending / confirmed / canceled

    class Config:
        from_attributes = True
