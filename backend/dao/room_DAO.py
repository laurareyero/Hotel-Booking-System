from models import Room
from database import get_connection
import logging as log

class RoomDAO:

    _SELECCIONAR = '''
        SELECT *
        FROM rooms
        ORDER BY id_room
    '''

    _INSERTAR = '''
        INSERT INTO rooms(
            room_number,
            room_type,
            price_per_night,
            status
        )
        VALUES(%s, %s, %s, %s)
    '''

    _ACTUALIZAR = '''
        UPDATE rooms
        SET
            room_number=%s,
            room_type=%s,
            price_per_night=%s,
            status=%s
        WHERE id_room=%s
    '''

    _ELIMINAR = '''
        DELETE FROM rooms
        WHERE id_room=%s
    '''

    @classmethod
    def insertar(cls, room: Room):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (
                        room.room_number,
                        room.room_type,
                        room.price_per_night,
                        room.status,
                    )
                    cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Inserted: {room}')
                    return cursor.rowcount
        except Exception as error: