from models import Booking
from database import get_connection
import logging as log

class BookingDAO:

    _SELECCIONAR = '''
        SELECT *
        FROM bookings
        ORDER BY id_booking
    '''

    _INSERTAR = '''
        INSERT INTO bookings(
            id_guest,
            id_room,
            check_in_date,
            check_out_date,
            total_price,
            status
        )
        VALUES(%s, %s, %s, %s, %s, %s)
    '''

    _ACTUALIZAR = '''
        UPDATE bookings
        SET
            id_guest=%s,
            id_room=%s,
            check_in_date=%s,
            check_out_date=%s,
            total_price=%s,
            status=%s
        WHERE id_booking=%s
    '''

    _ELIMINAR = '''
        DELETE FROM bookings
        WHERE id_booking=%s
    '''

    @classmethod
    def insertar(cls, booking: Booking):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (
                        booking.id_guest,
                        booking.id_room,
                        booking.check_in_date,
                        booking.check_out_date,
                        booking.total_price,
                        booking.status,
                    )
                    cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Inserted: {booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Insertion failed: {error}')
            raise

    @classmethod
    def seleccionar(cls):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()
                    return [Booking(*registro) for registro in registros]
        except Exception as error:
            log.error(f'Selection failed: {error}')
            raise

    @classmethod
    def actualizar(cls, booking: Booking):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (
                        booking.id_guest,
                        booking.id_room,
                        booking.check_in_date,
                        booking.check_out_date,
                        booking.total_price,
                        booking.status,
                        booking.id_booking,
                    )
                    cursor.execute(cls._ACTUALIZAR, valores)
                    log.debug(f'Updated: {booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Update failed: {error}')
            raise

    @classmethod
    def eliminar(cls, booking: Booking):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (booking.id_booking,)
                    cursor.execute(cls._ELIMINAR, valores)
                    log.debug(f'Deleted: {booking}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Deletion failed: {error}')
            raise