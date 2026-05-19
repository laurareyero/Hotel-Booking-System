import psycopg
from psycopg.errors import UniqueViolation, ForeignKeyViolation, NotNullViolation
from fastapi import HTTPException
from contextlib import contextmanager
import logging
import os 

@contextmanager
async def get_connection():
    conn = None
    try:
        conn = await psycopg.connect(os.getenv("DATABASE_URL"))
        yield conn
        conn.commit()
    except UniqueViolation as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=409, detail=str(e.diag.message_detail))
    except ForeignKeyViolation as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=409, detail="Referenced record does not exist.")
    except NotNullViolation as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=422, detail=f"Missing required field: {e.diag.column_name}")
    except Exception as e:
        if conn: conn.rollback()
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
    finally:
        if conn: conn.close()