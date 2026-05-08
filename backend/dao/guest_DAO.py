from models import Guest 
from database import get_connection
import logging as log

from models import Guest
from database import get_connection
import logging as log
 
class GuestDAO:
 
    _SELECCIONAR = "SELECT * FROM guests ORDER BY id_guest"
 
    _SELECCIONAR_POR_ID = "SELECT * FROM guests WHERE id_guest = %s"
 
    _INSERTAR = '''
        INSERT INTO guests(first_name, last_name, email, phone, dni)
        VALUES(%s, %s, %s, %s, %s)
    '''
 
    _ACTUALIZAR = '''
        UPDATE guests
        SET first_name=%s, last_name=%s, email=%s, phone=%s, dni=%s
        WHERE id_guest=%s
    '''
 
    _ELIMINAR = "DELETE FROM guests WHERE id_guest=%s"
 
    @classmethod
    def seleccionar(cls):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._SELECCIONAR)
                    registros = cursor.fetchall()
                    return [Guest(*registro) for registro in registros]
        except Exception as error:
            log.error(f'Selection failed: {error}')
            raise
 
    @classmethod
    def seleccionar_por_id(cls, id_guest: int):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._SELECCIONAR_POR_ID, (id_guest,))
                    registro = cursor.fetchone()
                    return Guest(*registro) if registro else None
        except Exception as error:
            log.error(f'Selection by id failed: {error}')
            raise
 
    @classmethod
    def insertar(cls, guest: Guest):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (guest.first_name, guest.last_name, guest.email, guest.phone, guest.dni)
                    cursor.execute(cls._INSERTAR, valores)
                    log.debug(f'Inserted: {guest}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Insertion failed: {error}')
            raise
 
    @classmethod
    def actualizar(cls, guest: Guest):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    valores = (guest.first_name, guest.last_name, guest.email, guest.phone, guest.dni, guest.id_guest)
                    cursor.execute(cls._ACTUALIZAR, valores)
                    log.debug(f'Updated: {guest}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Update failed: {error}')
            raise
 
    @classmethod
    def eliminar(cls, id_guest: int):
        try:
            with get_connection() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(cls._ELIMINAR, (id_guest,))
                    log.debug(f'Deleted guest id: {id_guest}')
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Deletion failed: {error}')
            raise