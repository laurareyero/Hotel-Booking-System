from fastapi import APIRouter, HTTPException
from models import Guest
from dao.guest_DAO import GuestDAO

router = APIRouter(tags=["Guests"])


# GET /guests
@router.get('/guests')
def get_guests():
    registros = GuestDAO.seleccionar()
    if not registros:
        raise HTTPException(status_code=404, detail='No guests found')
    return registros


# GET /guests/{id_guest}
@router.get('/guests/{id_guest}')
def get_guest(id_guest: int):
    guest = GuestDAO.seleccionar_por_id(id_guest)
    if not guest:
        raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')
    return guest


# POST /guests
@router.post('/guests')
def create_guest(guest: Guest):
    rows = GuestDAO.insertar(guest)
    if rows:
        return {'message': 'Guest created successfully'}
    raise HTTPException(status_code=500, detail='Failed to create guest')


# PUT /guests/{id_guest}
@router.put('/guests/{id_guest}')
def update_guest(id_guest: int, guest: Guest):
    guest.id_guest = id_guest
    rows = GuestDAO.actualizar(guest)
    if rows:
        return {'message': 'Guest updated successfully'}
    raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')


# DELETE /guests/{id_guest}
@router.delete('/guests/{id_guest}')
def delete_guest(id_guest: int):
    rows = GuestDAO.eliminar(id_guest)
    if rows:
        return {'message': 'Guest deleted successfully'}
    raise HTTPException(status_code=404, detail=f'Guest {id_guest} not found')


 
