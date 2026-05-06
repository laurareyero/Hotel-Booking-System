from fastapi import APIRouter
from booking import Booking
from booking_dao import BookingDAO
 
router = APIRouter()
 
 
# GET /reservations 
@router.get('/reservations')
def get_reservations(status: str = None):
    return BookingDAO.seleccionar(status=status)
 
 
# GET /reservations/{id} 
@router.get('/reservations/{id}')
def get_reservation(id: int):
    reservation = BookingDAO.seleccionar_por_id(id)
    if not reservation:
        return {'error': f'Reservation {id} not found'}
    return reservation
 
 
# POST /reservations 
@router.post('/reservations')
def create_reservation(booking: Booking):
    rows = BookingDAO.insertar(booking)
    if rows:
        return {'message': 'Reservation created successfully'}
    return {'error': 'Failed to create reservation'}
 
 
# PUT /reservations/{id} 
@router.put('/reservations/{id}')
def update_reservation(id: int, booking: Booking):
    existing = BookingDAO.seleccionar_por_id(id)
    if not existing:
        return {'error': f'Reservation {id} not found'}
    booking.id = id
    rows = BookingDAO.actualizar(booking)
    if rows:
        return {'message': 'Reservation updated successfully'}
    return {'error': 'Failed to update reservation'}
 
 
# DELETE /reservations/{id} 
@router.delete('/reservations/{id}')
def delete_reservation(id: int):
    existing = BookingDAO.seleccionar_por_id(id)
    if not existing:
        return {'error': f'Reservation {id} not found'}
    rows = BookingDAO.eliminar(existing)
    if rows:
        return {'message': 'Reservation deleted successfully'}
    return {'error': 'Failed to delete reservation'}