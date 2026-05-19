from fastapi import APIRouter
from models import Room
from dao.room_DAO import RoomDAO
from exceptions import RoomNotFoundError, RoomCreationError
from decorators import auditoria_endpoint

router = APIRouter(tags=["Rooms"])


@router.get('/rooms')
@auditoria_endpoint
async def get_rooms():
    registros = await RoomDAO.seleccionar()
    if not registros:
        raise RoomNotFoundError(0).to_http_exception()
    return registros


@router.get('/rooms/{id_room}')
@auditoria_endpoint
async def get_room(id_room: int):
    room = await RoomDAO.seleccionar_por_id(id_room)
    if not room:
        raise RoomNotFoundError(id_room).to_http_exception()
    return room


@router.post('/rooms')
@auditoria_endpoint
async def create_room(room: Room):
    rows = await RoomDAO.insertar(room)
    if rows:
        return {'message': 'Room created successfully'}
    raise RoomCreationError().to_http_exception()


@router.put('/rooms/{id_room}')
@auditoria_endpoint
async def update_room(id_room: int, room: Room):
    room.id_room = id_room
    rows = await RoomDAO.actualizar(room)
    if rows:
        return {'message': 'Room updated successfully'}
    raise RoomNotFoundError(id_room).to_http_exception()


@router.delete('/rooms/{id_room}')
@auditoria_endpoint
async def delete_room(id_room: int):
    rows = await RoomDAO.eliminar(id_room)
    if rows:
        return {'message': 'Room deleted successfully'}
    raise RoomNotFoundError(id_room).to_http_exception()