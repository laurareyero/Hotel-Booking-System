from fastapi import APIRouter, HTTPException
from models import Room
from dao.room_DAO import RoomDAO

router = APIRouter(tags=["Rooms"])


# GET /rooms
@router.get('/rooms')
async def get_rooms():
    registros = RoomDAO.seleccionar()
    if not registros:
        raise HTTPException(status_code=404, detail='No rooms found')
    return registros


# GET /rooms/{id_room}
@router.get('/rooms/{id_room}')
async def get_room(id_room: int):
    room = RoomDAO.seleccionar_por_id(id_room)
    if not room:
        raise HTTPException(status_code=404, detail=f'Room {id_room} not found')
    return room


# POST /rooms
@router.post('/rooms')
async def create_room(room: Room):
    rows = RoomDAO.insertar(room)
    if rows:
        return {'message': 'Room created successfully'}
    raise HTTPException(status_code=500, detail='Failed to create room')


# PUT /rooms/{id_room}
@router.put('/rooms/{id_room}')
async def update_room(id_room: int, room: Room):
    room.id_room = id_room
    rows = RoomDAO.actualizar(room)
    if rows:
        return {'message': 'Room updated successfully'}
    raise HTTPException(status_code=404, detail=f'Room {id_room} not found')


# DELETE /rooms/{id_room}
@router.delete('/rooms/{id_room}')
async def delete_room(id_room: int):
    rows = RoomDAO.eliminar(id_room)
    if rows:
        return {'message': 'Room deleted successfully'}
    raise HTTPException(status_code=404, detail=f'Room {id_room} not found')