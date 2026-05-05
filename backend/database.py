import psycopg
from psycopg import Error
from fastapi import HTTPException
from contextlib import contextmanager

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
    except Error as e:
        if conn:
            conn.rollback()
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Could not connect to the database")
    finally:
        if conn:
            conn.close()