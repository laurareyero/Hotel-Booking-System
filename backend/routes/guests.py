from fastapi import APIRouter
from models import Guest
from dao.guest_DAO import GuestDAO
from exceptions import GuestNotFoundError, GuestCreationError
from decorators import auditoria_endpoint
import logging as log

router = APIRouter(tags=["Guests"])


@router.get('/guests')
@auditoria_endpoint
async def get_guests():
    registros = await GuestDAO.seleccionar()
    if not registros:
        raise GuestNotFoundError(0).to_http_exception()
    return registros


@router.get('/guests/{id_guest}')
@auditoria_endpoint
async def get_guest(id_guest: int):
    guest = await GuestDAO.seleccionar_por_id(id_guest)
    if not guest:
        raise GuestNotFoundError(id_guest).to_http_exception()
    return guest


@router.post('/guests')
@auditoria_endpoint
async def create_guest(guest: Guest):
    rows = await GuestDAO.insertar(guest)
    if rows:
        return {'message': 'Guest created successfully'}
    raise GuestCreationError().to_http_exception()


@router.put('/guests/{id_guest}')
@auditoria_endpoint
async def update_guest(id_guest: int, guest: Guest):
    guest.id_guest = id_guest
    rows = await GuestDAO.actualizar(guest)
    if rows:
        return {'message': 'Guest updated successfully'}
    raise GuestNotFoundError(id_guest).to_http_exception()


@router.delete('/guests/{id_guest}')
@auditoria_endpoint
async def delete_guest(id_guest: int):
    rows = await GuestDAO.eliminar(id_guest)
    if rows:
        return {'message': 'Guest deleted successfully'}
    raise GuestNotFoundError(id_guest).to_http_exception()