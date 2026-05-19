from models import Guest
from database import get_connection
import logging as log


class GuestDAO:

    _SELECCIONAR = "SELECT * FROM guests ORDER BY id_guest"
    _SELECCIONAR_POR_ID = "SELECT * FROM guests WHERE id_guest = %s"
    _INSERTAR = "INSERT INTO guests(first_name, last_name, email, phone, dni) VALUES(%s, %s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE guests SET first_name=%s, last_name=%s, email=%s, phone=%s, dni=%s WHERE id_guest=%s"
    _ELIMINAR = "DELETE FROM guests WHERE id_guest=%s"

    @classmethod
    async def seleccionar(cls):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR)
                    registros = await cursor.fetchall()
                    return [Guest(id_guest=r[0], first_name=r[1], last_name=r[2], email=r[3], phone=r[4], dni=r[5]) for r in registros]
        except Exception as error:
            log.error(f'Selection failed: {error}')
            raise

    @classmethod
    async def seleccionar_por_id(cls, id_guest: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._SELECCIONAR_POR_ID, (id_guest,))
                    r = await cursor.fetchone()
                    return Guest(id_guest=r[0], first_name=r[1], last_name=r[2], email=r[3], phone=r[4], dni=r[5]) if r else None
        except Exception as error:
            log.error(f'Selection by id failed: {error}')
            raise

    @classmethod
    async def insertar(cls, guest: Guest):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._INSERTAR, (guest.first_name, guest.last_name, guest.email, guest.phone, guest.dni))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Insertion failed: {error}')
            raise

    @classmethod
    async def actualizar(cls, guest: Guest):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._ACTUALIZAR, (guest.first_name, guest.last_name, guest.email, guest.phone, guest.dni, guest.id_guest))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Update failed: {error}')
            raise

    @classmethod
    async def eliminar(cls, id_guest: int):
        try:
            async with get_connection() as conexion:
                async with conexion.cursor() as cursor:
                    await cursor.execute(cls._ELIMINAR, (id_guest,))
                    return cursor.rowcount
        except Exception as error:
            log.error(f'Deletion failed: {error}')
            raise
