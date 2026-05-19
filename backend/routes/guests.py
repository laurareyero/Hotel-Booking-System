from fastapi import APIRouter, HTTPException
from models import Guest
from dao.guest_DAO import GuestDAO
import logging as log

router = APIRouter(tags=["Guests"])


# GET /guests
@router.get('/guests')
async def get_guests():
    registros = GuestDAO.seleccionar()
    if not registros:
        raise HTTPException(status_code=404, detail='No guests found')
    return registros


# GET /guests/{id_guest}
@router.get('/guests/{id_guest}')
async def get_guest(id_guest: int):
    guest = GuestDAO.seleccionar_por_id(id_guest)
    if not guest:
        raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')
    return guest


# POST /guests
@router.post('/guests')
async def create_guest(guest: Guest):
    log.info(f'Creating guest {guest.first_name} {guest.last_name}')
    rows = GuestDAO.insertar(guest)
    if rows:
        return {'message': 'Guest created successfully'}
    raise HTTPException(status_code=500, detail='Failed to create guest')


# PUT /guests/{id_guest}
@router.put('/guests/{id_guest}')
async def update_guest(id_guest: int, guest: Guest):
    log.info(f'Updating guest {id_guest}')
    guest.id_guest = id_guest
    rows = GuestDAO.actualizar(guest)
    if rows:
        log.info(f'Guest {id_guest} updated successfully')
        return {'message': 'Guest updated successfully'}
    log.warning(f'Guest {id_guest} not found')
    raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')


# DELETE /guests/{id_guest}
@router.delete('/guests/{id_guest}')
async def delete_guest(id_guest: int):
    log.info(f'Deleting guest {id_guest}')
    rows = GuestDAO.eliminar(id_guest)
    if rows:
        return {'message': 'Guest deleted successfully'}
    log.warning(f'Guest {id_guest} not found')
    raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')


 
