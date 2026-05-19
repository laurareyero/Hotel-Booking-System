import logging
import functools

log = logging.getLogger(__name__)

def auditoria_endpoint(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        log.info(f"[{func.__name__}] called with kwargs={kwargs}")
        try:
            result = await func(*args, **kwargs)
            log.info(f"[{func.__name__}] completed successfully")
            return result
        except Exception as e:
            log.error(f"[{func.__name__}] failed: {e}")
            raise
    return wrapper