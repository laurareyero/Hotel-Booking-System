from conexion import Conexion
from persona import Persona
from logger_base import log


class PersonaDAO:

    _SELECCIONAR = '''
        SELECT *
        FROM guests
        ORDER BY id
    '''

    _INSERTAR = '''
        INSERT INTO guests(
            first_name,
            last_name,
            email,
            phone,
            dni
        )
        VALUES(%s, %s, %s, %s, %s)
    '''

    _ACTUALIZAR = '''
        UPDATE guests
        SET
            first_name=%s,
            last_name=%s,
            email=%s,
            phone=%s,
            dni=%s
        WHERE id=%s
    '''

    _ELIMINAR = '''
        DELETE FROM guests
        WHERE id=%s
    '''

    @classmethod
    def insertar(cls, persona):                         

        try:

            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:

                    valores = (
                        persona.first_name,             
                        persona.last_name,               
                        persona.email,                  
                        persona.phone,
                        persona.dni,
                    )

                    cursor.execute(cls._INSERTAR, valores)

                    log.debug(f'Inserted: {persona}')

                    return cursor.rowcount

        except Exception as error:

            log.error(f'Insertion failed: {error}')

            raise


    @classmethod
    def seleccionar(cls):

        try:

            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:

                    cursor.execute(cls._SELECCIONAR)

                    registros = cursor.fetchall()

                    return [Persona(*registro) for registro in registros]

        except Exception as error:

            log.error(f'Selection failed: {error}')

            raise


    @classmethod
    def actualizar(cls, persona):

        try:

            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:

                    valores = (
                        persona.first_name,             
                        persona.last_name,              
                        persona.email,                   
                        persona.phone,
                        persona.dni,
                        persona.id,                     
                    )

                    cursor.execute(cls._ACTUALIZAR, valores)

                    log.debug(f'Updated: {persona}')

                    return cursor.rowcount

        except Exception as error:

            log.error(f'Update failed: {error}')

            raise


    @classmethod
    def eliminar(cls, persona):

        try:

            with Conexion.obtenerConexion() as conexion:
                with conexion.cursor() as cursor:

                    valores = (persona.id,)              
                                                         

                    cursor.execute(cls._ELIMINAR, valores)

                    log.debug(f'Deleted: {persona}')

                    return cursor.rowcount

        except Exception as error:

            log.error(f'Deletion failed: {error}')

            raise



 