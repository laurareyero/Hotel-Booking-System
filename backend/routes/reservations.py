from fastapi import APIRouter, HTTPException
from booking_DAO import BookingDAO
from models import Booking 


router = APIRouter()
 
 
# GET /bookings  
@router.get('/bookings')
def get_bookings(status: str = None):
    return BookingDAO.seleccionar(status=status)
 
 
# GET /bookings/{id} 
@router.get('/bookings/{id}')
def get_booking(id: int):
    booking = BookingDAO.seleccionar_por_id(id)
    if not booking:
        return {'error': f'Booking {id} not found'}
    return booking
 
 
# POST /bookings 
@router.post('/bookings')
def create_booking(booking: Booking):
    rows = BookingDAO.insertar(booking)
    if rows:
        return {'message': 'Booking created successfully'}
    return {'error': 'Failed to create booking'}
 
 
# PUT /bookings/{id} 
@router.put('/bookings/{id}')
def update_booking(id: int, booking: Booking):
    existing = BookingDAO.seleccionar_por_id(id)
    if not existing:
        return {'error': f'Booking {id} not found'}
    booking.id = id
    rows = BookingDAO.actualizar(booking)
    if rows:
        return {'message': 'Booking updated successfully'}
    return {'error': 'Failed to update booking'}
 
 
# DELETE /bookings/{id} 
@router.delete('/bookings/{id}')
def delete_booking(id: int):
    existing = BookingDAO.seleccionar_por_id(id)
    if not existing:
        return {'error': f'Booking {id} not found'}
    rows = BookingDAO.eliminar(existing)
    if rows:
        return {'message': 'Booking deleted successfully'}
    return {'error': 'Failed to delete booking'}