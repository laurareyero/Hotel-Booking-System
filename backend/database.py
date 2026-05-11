import psycopg
from psycopg import Error
from psycopg.errors import UniqueViolation, ForeignKeyViolation, NotNullViolation
from fastapi import HTTPException
from contextlib import contextmanager
import logging

@contextmanager
def get_connection():
    conn = None
    try:
        conn = psycopg.connect(
            host="localhost",
            dbname="hotel_db",
            user="postgres",
            password="DataBase"
        )
        yield conn
        conn.commit()
    except UniqueViolation as e:
        if conn:
            conn.rollback()
        # Parse which field is duplicated from the error detail
        detail = str(e.diag.message_detail) if e.diag.message_detail else str(e)
        logging.warning(f"Unique constraint violation: {detail}")
        raise HTTPException(status_code=409, detail=f"Duplicate value: {detail}")
    except ForeignKeyViolation as e:
        if conn:
            conn.rollback()
        logging.warning(f"Foreign key violation: {e}")
        raise HTTPException(status_code=409, detail="Referenced record does not exist.")
    except NotNullViolation as e:
        if conn:
            conn.rollback()
        logging.warning(f"Not null violation: {e}")
        raise HTTPException(status_code=422, detail=f"Missing required field: {e.diag.column_name}")
    except Error as e:
        if conn:
            conn.rollback()
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
    finally:
        if conn:
            conn.close()