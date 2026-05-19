import streamlit as st
from src.api_client import get_guests, get_rooms, get_bookings

st.set_page_config(
    page_title="Hotel Booking System",
    layout="wide"
)

with st.sidebar:
    st.image("hotel.png", use_container_width=True)

st.title("🛎️ Hotel Booking System")
st.divider()

#  Datos 
guests = get_guests()
rooms = get_rooms()
bookings = get_bookings()

available = [r for r in rooms if r["status"] == "available"]
occupied  = [r for r in rooms if r["status"] == "occupied"]
maintenance = [r for r in rooms if r["status"] == "maintenance"]

confirmed  = [b for b in bookings if b["status"] == "confirmed"]
pending    = [b for b in bookings if b["status"] == "pending"]
cancelled  = [b for b in bookings if b["status"] == "cancelled"]
completed  = [b for b in bookings if b["status"] == "completed"]

# --- Métricas ---
st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Guests",     len(guests))
col2.metric("🛏️ Rooms",      len(rooms))
col3.metric("📖 Bookings",   len(bookings))

st.divider()
# Estado de reservas 
st.subheader("📖 Booking Status")
col1, col2, col3, col4 = st.columns(4)
col1.metric("⏳ Pending",    len(pending))
col2.metric("✅ Confirmed",  len(confirmed))
col3.metric("❌ Cancelled",  len(cancelled))
col4.metric("🏁 Completed",  len(completed))

st.divider()

st.page_link("pages/1_Guests.py",   label="👥 Guests")
st.page_link("pages/2_Rooms.py",    label="🛏️ Rooms")
st.page_link("pages/3_Bookings.py", label="📖 Bookings")