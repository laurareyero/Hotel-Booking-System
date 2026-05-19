from models import Room
from database import get_connection
import logging as log


class RoomDAO:

    _SELECCIONAR = "SELECT * FROM rooms ORDER BY id_room"
    _SELECCIONAR_POR_ID = "SELECT * FROM rooms WHERE id_room = %s"
    _INSERTAR = "INSERT INTO rooms(room_number, room_type, price_per_night, status) VALUES(%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE rooms SET room_number=%s, room_type=%s, price_per_night=%s, status=%s WHERE id_room=%s"
    _ELIMINAR = "DELETE FROM rooms WHERE id_room=%s"

    @classmethod
    async def seleccionar(cls):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR)
                    registros = await cursor.fetchall()
                    return [Room(id_room=r[0], room_number=r[1], room_type=r[2], price_per_night=r[3], status=r[4]) for r in registros]
        except Exception as error:
            log.error(f'Selection failed: {error}')
            raise

    @classmethod
    async def seleccionar_por_id(cls, id_room: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR_POR_ID, (id_room,))
                    r = await cursor.fetchone()
                    return Room(id_room=r[0], room_number=r[1], room_type=r[2], price_per_night=r[3], status=r[4]) if r else None
        except Exception as error:
            log.error(f'Selection by id failed: {error}')
            raise

    @classmethod
    async def insertar(cls, room: Room):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._INSERTAR, (room.room_number, room.room_type, room.price_per_night, room.status))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Insertion failed: {error}')
            raise

    @classmethod
    async def actualizar(cls, room: Room):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._ACTUALIZAR, (room.room_number, room.room_type, room.price_per_night, room.status, room.id_room))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Update failed: {error}')
            raise

    @classmethod
    async def eliminar(cls, id_room: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._ELIMINAR, (id_room,))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Deletion failed: {error}')
            raise