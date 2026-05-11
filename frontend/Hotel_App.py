import streamlit as st
from src.api_client import get_guests, get_rooms, get_bookings

st.set_page_config(
    page_title=" Hotel Booking System",
    layout="wide"
)
with st.sidebar:
    st.image("hotel.png", use_container_width=True)
    
st.title(" 🛎️ Hotel Booking System")

st.markdown("""
Welcome to the hotel management platform

Choose an option:
""")

st.page_link("pages/1_Guests.py",label=" Guests")
st.page_link("pages/2_Rooms.py", label="Rooms")
st.page_link("pages/3_Bookings.py", label="Bookings")


guests = get_guests()
rooms = get_rooms()
bookings = get_bookings()

st.metric("Guests", len(guests))
st.metric("Rooms", len(rooms))
st.metric("Bookings", len(bookings))