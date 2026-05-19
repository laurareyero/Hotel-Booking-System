from models import Booking
from database import get_connection
import logging as log
 
 
class BookingDAO:
 
    _SELECCIONAR = "SELECT * FROM bookings ORDER BY id_booking"
 
    _SELECCIONAR_POR_ID = "SELECT * FROM bookings WHERE id_booking = %s"
 
    _INSERTAR = '''
        INSERT INTO bookings(id_guest, id_room, check_in_date, check_out_date, total_price, status)
        VALUES(%s, %s, %s, %s, %s, %s)
    '''
 
    _ACTUALIZAR = '''
        UPDATE bookings
        SET id_guest=%s, id_room=%s, check_in_date=%s, check_out_date=%s, total_price=%s, status=%s
        WHERE id_booking=%s
    '''
 
    _SELECCIONAR_ACTIVAS_POR_ROOM = """
    SELECT * FROM bookings 
    WHERE id_room = %s AND status = 'confirmed'
    """
 
    @classmethod
    async def seleccionar(cls):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR)
                    registros = await cursor.fetchall()
                    return [Booking(id_booking=r[0], id_guest=r[1], id_room=r[2], check_in_date=str(r[3]), check_out_date=str(r[4]), total_price=r[5], status=r[6]) for r in registros]
        except Exception as error:
            log.error(f'Selection failed: {error}')
            raise
 
    @classmethod
    async def seleccionar_por_id(cls, id_booking: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR_POR_ID, (id_booking,))
                    registro = await cursor.fetchone()
                    return Booking(id_booking=registro[0], id_guest=registro[1], id_room=registro[2], check_in_date=str(registro[3]), check_out_date=str(registro[4]), total_price=registro[5], status=registro[6]) if registro else None
        except Exception as error:
            log.error(f'Selection by id failed: {error}')
            raise
 
    @classmethod
    async def insertar(cls, booking: Booking):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    valores = (
                        booking.id_guest, booking.id_room,
                        booking.check_in_date, booking.check_out_date,
                        booking.total_price, booking.status,
                    )
                    await cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Inserted: {booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Insertion failed: {error}')
            raise
 
    @classmethod
    async def actualizar(cls, booking: Booking):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    valores = (
                        booking.id_guest, booking.id_room,
                        booking.check_in_date, booking.check_out_date,
                        booking.total_price, booking.status,
                        booking.id_booking,
                    )
                    await cursor.execute(cls._ACTUALIZAR, valores)
                    log.debug(f'Updated: {booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Update failed: {error}')
            raise
 
    @classmethod
    async def eliminar(cls, id_booking: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._ELIMINAR, (id_booking,))
                    log.debug(f'Deleted booking id: {id_booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Deletion failed: {error}')
            raise 
    @classmethod
    async def seleccionar_activas_por_room(cls, id_room: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR_ACTIVAS_POR_ROOM, (id_room,))
                    return await cursor.fetchall()
        except Exception as error:
            log.error(f'Selection by room failed: {error}')
            raise