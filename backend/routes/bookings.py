from fastapi import APIRouter, HTTPException
from dao.booking_DAO import BookingDAO
from models import Booking 
from dao.room_DAO import RoomDAO
import logging as log


router = APIRouter(tags=["Bookings"])

# GET /bookings  
@router.get('/bookings')
def get_bookings():
    log.info(f'Fetching all bookings')
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
    room = RoomDAO.seleccionar_por_id(booking.id_room)
    if not room:
        raise HTTPException(status_code=404, detail=f'Room {booking.id_room} not found')
    if room.status != 'available':
        raise HTTPException(status_code=400, detail=f'Room {booking.id_room} is not available')
    
    rows = BookingDAO.insertar(booking)
    if not rows:
        raise HTTPException(status_code=500, detail='Failed to create booking')
    
    room.status = 'occupied'
    RoomDAO.actualizar(room)
    
    return {'message': 'Booking created successfully'}

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
    if not rows:
        raise HTTPException(status_code=500, detail='Failed to delete booking')
    
    # Habitación vuelve a available
    room = RoomDAO.seleccionar_por_id(existing.id_room)
    if room:
        room.status = 'available'
        RoomDAO.actualizar(room)
    
    return {'message': 'Booking deleted successfully'}


# PATCH /bookings/{id_booking}/status
@router.patch('/bookings/{id_booking}/status')
def update_booking_status(id_booking: int, status: str):
    valid_statuses = ['pending', 'confirmed', 'cancelled', 'completed']
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f'Invalid status: {status}')

    existing = BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise HTTPException(status_code=404, detail=f'Booking {id_booking} not found')

    existing.status = status
    BookingDAO.actualizar(existing)

    room = RoomDAO.seleccionar_por_id(existing.id_room)
    if room:
        if status == 'confirmed':
            room.status = 'occupied'
        elif status in ['cancelled', 'completed']:
            # Solo liberar si no hay otras reservas confirmadas en esa habitación
            otras_activas = BookingDAO.seleccionar_activas_por_room(existing.id_room)
            otras_activas = [r for r in otras_activas if r[0] != id_booking]
            if not otras_activas:
                room.status = 'available'
        # 'completed y cancelled ' revierten el status de la habitación
        RoomDAO.actualizar(room)

    return {'message': 'Status updated successfully'}