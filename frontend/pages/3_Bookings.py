import streamlit as st
import pandas as pd
from src.sidebar import show_sidebar
show_sidebar()
from src.api_client import (
    get_bookings,
    create_booking,
    update_booking,
    delete_booking,
    update_booking_status,
    get_room 
)

st.title(" 📖 Bookings")
bookings = get_bookings()
# Bookings visual
st.subheader("Overview")
n_cols = 4
for i in range(0, len(bookings), n_cols):
    cols = st.columns(n_cols)
    batch = bookings[i:i + n_cols]
    for j, booking in enumerate(batch):
        room = get_room(booking["id_room"])
        with cols[j]:
            with st.container(border=True):
                st.markdown(f"**Booking {booking['id_booking']}**")
                st.caption(f"Guest ID: {booking['id_guest']}")
                st.caption(f"Room ID: {booking['id_room']}")
                if room:
                    st.caption(f"{room['room_type'].title()} - €{room['price_per_night']}/night")
                match booking["status"]:
                    case "pending":
                        st.markdown(":orange[● Pending]")
                    case "confirmed":
                        st.markdown(":green[● Confirmed]")
                    case "cancelled":
                        st.markdown(":red[● Cancelled]")
                    case "completed":
                        st.markdown(":blue[● Completed]")
                    case _:
                        st.markdown(":grey[● Unknown]")

st.divider()

# Create
st.subheader("➕ Create booking")

col1, col2 = st.columns(2)
with col1:
    guest_id = st.number_input("Guest ID", min_value=1, step=1)
    check_in = st.date_input("Check-in date")
with col2:
    room_id = st.number_input("Room ID", min_value=1, step=1)
    check_out = st.date_input("Check-out date")

# Calculamos el total automáticamente
total = 0.0
if check_out > check_in:
    room = get_room(room_id)
    if room:
        nights = (check_out - check_in).days
        total = nights * room["price_per_night"]
        st.info(f" {nights} nights × €{room['price_per_night']}/night = **€{total:.2f}**")
    else:
        st.warning("Room not found")
elif check_out <= check_in:
    st.error("Check-out must be after check-in")

status = st.selectbox("Status", ["pending", "confirmed", "cancelled", "completed"])

if st.button("➕ Create booking"):
    if check_out <= check_in:
        st.error("Fix the dates before creating")
    else:
        with st.spinner("Creating booking..."):
            response = create_booking({
                "id_guest": guest_id,
                "id_room": room_id,
                "check_in_date": str(check_in),
                "check_out_date": str(check_out),
                "total_price": total,
                "status": status
            })
        if response.status_code == 200:
            st.success("Booking created")
            st.balloons()
        else:
            st.error(f'Error creating booking')

# Show 
st.subheader(" 📋 Booking list")

if st.button(" 🔍 Show bookings"):
    bookings = get_bookings()

    if bookings:
        df = pd.DataFrame(bookings)
        st.dataframe(df)
    else:
        st.info(" ℹ️ No bookings found")


# Update 
st.subheader(" 🔄 Update booking")

update_id = st.number_input("Booking ID to update", min_value=1, step=1)

col1, col2 = st.columns(2)
with col1:
    new_guest_id = st.number_input("New Guest ID", min_value=1, step=1)
    new_check_in = st.date_input("New check-in date")
with col2:
    new_room_id = st.number_input("New Room ID", min_value=1, step=1)
    new_check_out = st.date_input("New check-out date")

# Calcular total sugerido
suggested_total = 0.0
if new_check_out > new_check_in:
    room = get_room(new_room_id)
    if room:
        nights = (new_check_out - new_check_in).days
        suggested_total = nights * room["price_per_night"]
        st.info(f"{nights} nights × €{room['price_per_night']}/night = **€{suggested_total:.2f}**")
    else:
        st.warning("Room not found")
elif new_check_out <= new_check_in:
    st.error("Check-out must be after check-in")

# El gestor puede dejarlo o modificarlo
new_total = st.number_input("Total price (€)", min_value=0.0, step=0.01, value=suggested_total)
new_status = st.selectbox("New status", ["pending", "confirmed", "cancelled", "completed"])

if st.button(" 🔄 Update Booking"):
    if new_check_out <= new_check_in:
        st.error("Fix the dates before updating")
    else:
        with st.spinner("Updating booking..."):
            response = update_booking(update_id, {
                "id_guest": new_guest_id,
                "id_room": new_room_id,
                "check_in_date": str(new_check_in),
                "check_out_date": str(new_check_out),
                "total_price": new_total,
                "status": new_status
            })
        if response.status_code == 200:
            st.success("Booking updated")
        else:
            st.error("Error updating booking")


# Delete 
st.subheader("🗑️ Delete booking")

delete_id = st.number_input("Booking ID to delete", min_value=1, step=1)

if st.button("🗑️ Delete booking"):
    response = delete_booking(delete_id)

    if response.status_code == 200:
        st.success("Booking deleted")
    else:
        st.error("Error deleting booking")
        

#Change only status 
st.subheader("Change booking status")

status_id = st.number_input("Booking ID", min_value=1, step=1, key="status_id")
patch_status = st.selectbox("Select new status", ["pending", "confirmed", "cancelled", "completed"])

if st.button("Update status"):
    response = update_booking_status(status_id, patch_status)
    if response.status_code == 200:
        st.toast("Status updated! ✅")
    else:
        st.error("Error updating status")