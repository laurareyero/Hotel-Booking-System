import streamlit as st
from src.api_client import get_guests, get_rooms, get_bookings

guests = get_guests()
rooms = get_rooms()
bookings = get_bookings()

st.metric("Guests", len(guests))
st.metric("Rooms", len(rooms))
st.metric("Bookings", len(bookings))