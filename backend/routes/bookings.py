from fastapi import APIRouter, HTTPException
from booking_DAO import BookingDAO
from models import Booking 


router = APIRouter()
 
 
# GET /bookings  
@router.get('/bookings')
def get_bookings():
    registros = BookingDAO.seleccionar()
    if not registros:
        raise HTTPException(status_code=404, detail='No bookings found')
    return registros
 
 
# GET /bookings/{id_booking:int} 
@router.get('/bookings/{id_booking:int}')
def get_booking(id_booking: int):
    booking = BookingDAO.seleccionar_por_id(id_booking)
    if not booking:
        raise HTTPException(status_code=404, detail=f'Booking {id_booking} not found')
    return booking
 
 
# POST /bookings 
@router.post('/bookings')
def create_booking(booking: Booking):
    rows = BookingDAO.insertar(booking)
    if rows:
        return {'message': 'Booking created successfully'}
    raise HTTPException(status_code=500, detail='Failed to create booking')


# PUT /bookings/{id_booking:int} 
@router.put('/bookings/{id_booking:int}')
def update_booking(id_booking: int, booking: Booking):
    existing = BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise HTTPException(status_code=404, detail=f'Booking {id_booking} not found')
    booking.id_booking = id_booking
    rows = BookingDAO.actualizar(booking)
    if rows:
        return {'message': 'Booking updated successfully'}
    raise HTTPException(status_code=500, detail='Failed to update booking')


# DELETE /bookings/{id_booking:int}
@router.delete('/bookings/{id_booking:int}')
def delete_booking(id_booking: int):
    existing = BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise HTTPException(status_code=404, detail=f'Booking {id_booking} not found')
    rows = BookingDAO.eliminar(id_booking)
    if rows:
        return {'message': 'Booking deleted successfully'}
    raise HTTPException(status_code=500, detail='Failed to delete booking')