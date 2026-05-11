import requests

import os
BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def get_guests():
    response = requests.get(f"{BASE_URL}/guests")
    if response.status_code == 200:
        return response.json()
    return []


def get_guest(id_guest: int):
    response = requests.get(f"{BASE_URL}/guests/{id_guest}")
    if response.status_code == 200:
        return response.json()
    return None


def create_guest(data: dict):
    response = requests.post(f"{BASE_URL}/guests", json=data)
    return response


def update_guest(id_guest: int, data: dict):
    response = requests.put(f"{BASE_URL}/guests/{id_guest}", json=data)
    return response


def delete_guest(id_guest: int):
    response = requests.delete(f"{BASE_URL}/guests/{id_guest}")
    return response



def get_rooms():
    response = requests.get(f"{BASE_URL}/rooms")
    if response.status_code == 200:
        return response.json()
    return []


def get_room(id_room: int):
    response = requests.get(f"{BASE_URL}/rooms/{id_room}")
    if response.status_code == 200:
        return response.json()
    return None


def get_bookings():
    response = requests.get(f"{BASE_URL}/bookings")
    if response.status_code == 200:
        return response.json()
    return []


def get_booking(id_booking: int):
    response = requests.get(f"{BASE_URL}/bookings/{id_booking}")
    if response.status_code == 200:
        return response.json()
    return None


def create_booking(data: dict):
    response = requests.post(f"{BASE_URL}/bookings", json=data)
    return response


def update_booking(id_booking: int, data: dict):
    response = requests.put(f"{BASE_URL}/bookings/{id_booking}", json=data)
    return response


def delete_booking(id_booking: int):
    response = requests.delete(f"{BASE_URL}/bookings/{id_booking}")
    return response

def create_room(data: dict):
    response = requests.post(f"{BASE_URL}/rooms", json=data)
    return response

def update_room(id_room: int, data: dict):
    response = requests.put(f"{BASE_URL}/rooms/{id_room}", json=data)
    return response

def delete_room(id_room: int):
    response = requests.delete(f"{BASE_URL}/rooms/{id_room}")
    return response