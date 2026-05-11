import psycopg
from psycopg.errors import UniqueViolation, ForeignKeyViolation, NotNullViolation
from fastapi import HTTPException
from contextlib import contextmanager
import logging

@contextmanager
def get_connection():
    conn = None
    try:
        conn = psycopg.connect("postgresql://postgres.ijgnuxwklohewhhhoygm:DataBASE2356_@aws-0-eu-west-1.pooler.supabase.com:5432/postgres")
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