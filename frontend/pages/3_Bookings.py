import streamlit as st
import pandas as pd

from src.sidebar import show_sidebar
show_sidebar()
from src.api_client import (
    get_bookings,
    create_booking,
    update_booking,
    delete_booking,
    update_booking_status
)

st.title(" 📖 Reservations")

# Create
st.subheader("➕ Create reservation")

col1, col2 = st.columns(2)
with col1:
    guest_id = st.number_input("Guest ID", min_value=1, step=1)
    check_in = st.date_input("Check-in date")
    total = st.number_input("Total price", min_value=0.0, step=0.01, value=0.0)
with col2:
    room_id = st.number_input("Room ID", min_value=1, step=1)
    check_out = st.date_input("Check-out date")
    status = st.selectbox("Status", ["pending", "confirmed", "cancelled", "completed"])

if st.button("➕ Create reservation"):
    with st.spinner("Creating reservation..."):
        response = create_booking({
            "id_guest": guest_id,
            "id_room": room_id,
            "check_in_date": str(check_in),
            "check_out_date": str(check_out),
            "total_price": total,
            "status": status
        })
    if response.status_code == 200:
        st.success("Reservation created")
        st.balloons()
    else:
        st.error(f'Error creating reservation')


# Show 
st.subheader(" 📋 Reservation list")

if st.button(" 🔍 Show reservations"):
    bookings = get_bookings()

    if bookings:
        df = pd.DataFrame(bookings)
        st.dataframe(df)
    else:
        st.info(" ℹ️ No reservations found")


# Update 
st.subheader(" 🔄 Update reservation")

update_id = st.number_input("Reservation ID to update", min_value=1, step=1)

col1, col2 = st.columns(2)
with col1:
    new_guest_id = st.number_input("New Guest ID", min_value=1, step=1)
    new_check_in = st.date_input("New check-in date")
    new_total = st.number_input("New total price", min_value=0.0, step=0.01, value=0.0)
with col2:
    new_room_id = st.number_input("New Room ID", min_value=1, step=1)
    new_check_out = st.date_input("New check-out date")
    new_status = st.selectbox("New status", ["pending", "confirmed", "cancelled", "completed"])

if st.button(" 🔄 Update reservation"):
    with st.spinner("Updating reservation..."):
        response = update_booking(update_id, {
            "id_guest": new_guest_id,
            "id_room": new_room_id,
            "check_in_date": str(new_check_in),
            "check_out_date": str(new_check_out),
            "total_price": new_total,
            "status": new_status
        })
    if response.status_code == 200:
        st.success("Reservation updated")
    else:
        st.error("Error updating reservation")


# Delete 
st.subheader("❌ Delete reservation")

delete_id = st.number_input("Reservation ID to delete", min_value=1, step=1)

if st.button("❌ Delete reservation"):
    response = delete_booking(delete_id)

    if response.status_code == 200:
        st.success("Reservation deleted")
    else:
        st.error("Error deleting reservation")
        

#Change only status 
st.subheader("🔄 Change reservation status")

status_id = st.number_input("Reservation ID", min_value=1, step=1)
new_status = st.selectbox("Select new status", ["pending", "confirmed", "cancelled", "completed"])

if st.button("Update status"):
    with st.spinner("Updating status..."):
        response = update_booking_status(status_id, new_status)
    if response.status_code == 200:
        st.toast("Status updated! ✅")
    else:
        st.error("Error updating status")