from fastapi import HTTPException


class HotelError(Exception):
    def __init__(self, mensaje: str, status_code: int):
        self.mensaje = mensaje
        self.status_code = status_code

    def to_http_exception(self):
        return HTTPException(status_code=self.status_code, detail=self.mensaje)


class GuestNotFoundError(HotelError):
    def __init__(self, id_guest: int):
        super().__init__(f"Guest {id_guest} not found", 404)

class GuestCreationError(HotelError):
    def __init__(self):
        super().__init__("Failed to create guest", 500)

class RoomNotFoundError(HotelError):
    def __init__(self, id_room: int):
        super().__init__(f"Room {id_room} not found", 404)

class RoomNotAvailableError(HotelError):
    def __init__(self, id_room: int):
        super().__init__(f"Room {id_room} is not available", 400)

class RoomCreationError(HotelError):
    def __init__(self):
        super().__init__("Failed to create room", 500)

class BookingNotFoundError(HotelError):
    def __init__(self, id_booking: int):
        super().__init__(f"Booking {id_booking} not found", 404)

class BookingCreationError(HotelError):
    def __init__(self):
        super().__init__("Failed to create booking", 500)

class InvalidStatusError(HotelError):
    def __init__(self, status: str):
        super().__init__(f"Invalid status: {status}", 400)