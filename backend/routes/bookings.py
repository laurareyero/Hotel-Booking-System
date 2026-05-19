from fastapi import APIRouter
from dao.booking_DAO import BookingDAO
from dao.room_DAO import RoomDAO
from models import Booking
from exceptions import (
    BookingNotFoundError, BookingCreationError,
    RoomNotFoundError, RoomNotAvailableError, InvalidStatusError
)
from decorators import auditoria_endpoint
import logging as log

router = APIRouter(tags=["Bookings"])

VALID_STATUSES = ['pending', 'confirmed', 'cancelled', 'completed']


@router.get('/bookings')
@auditoria_endpoint
async def get_bookings():
    registros = await BookingDAO.seleccionar()
    if not registros:
        raise BookingNotFoundError(0).to_http_exception()
    return registros


@router.get('/bookings/{id_booking}')
@auditoria_endpoint
async def get_booking(id_booking: int):
    booking = await BookingDAO.seleccionar_por_id(id_booking)
    if not booking:
        raise BookingNotFoundError(id_booking).to_http_exception()
    return booking


@router.post('/bookings')
@auditoria_endpoint
async def create_booking(booking: Booking):
    room = await RoomDAO.seleccionar_por_id(booking.id_room)
    if not room:
        raise RoomNotFoundError(booking.id_room).to_http_exception()
    if room.status != 'available':
        raise RoomNotAvailableError(booking.id_room).to_http_exception()
    rows = await BookingDAO.insertar(booking)
    if not rows:
        raise BookingCreationError().to_http_exception()
    room.status = 'occupied'
    await RoomDAO.actualizar(room)
    return {'message': 'Booking created successfully'}


@router.put('/bookings/{id_booking}')
@auditoria_endpoint
async def update_booking(id_booking: int, booking: Booking):
    existing = await BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise BookingNotFoundError(id_booking).to_http_exception()
    booking.id_booking = id_booking
    rows = await BookingDAO.actualizar(booking)
    if rows:
        return {'message': 'Booking updated successfully'}
    raise BookingNotFoundError(id_booking).to_http_exception()


@router.delete('/bookings/{id_booking}')
@auditoria_endpoint
async def delete_booking(id_booking: int):
    existing = await BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise BookingNotFoundError(id_booking).to_http_exception()
    rows = await BookingDAO.eliminar(id_booking)
    if not rows:
        raise BookingNotFoundError(id_booking).to_http_exception()
    room = await RoomDAO.seleccionar_por_id(existing.id_room)
    if room:
        room.status = 'available'
        await RoomDAO.actualizar(room)
    return {'message': 'Booking deleted successfully'}


@router.patch('/bookings/{id_booking}/status')
@auditoria_endpoint
async def update_booking_status(id_booking: int, status: str):
    if status not in VALID_STATUSES:
        raise InvalidStatusError(status).to_http_exception()
    existing = await BookingDAO.seleccionar_por_id(id_booking)
    if not existing:
        raise BookingNotFoundError(id_booking).to_http_exception()
    existing.status = status
    await BookingDAO.actualizar(existing)
    room = await RoomDAO.seleccionar_por_id(existing.id_room)
    if room:
        if status == 'confirmed':
            room.status = 'occupied'
        elif status in ['cancelled', 'completed']:
            otras_activas = await BookingDAO.seleccionar_activas_por_room(existing.id_room)
            otras_activas = [r for r in otras_activas if r[0] != id_booking]
            if not otras_activas:
                room.status = 'available'
        await RoomDAO.actualizar(room)
    return {'message': 'Status updated successfully'}