import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rooms", layout="wide")

from src.sidebar import show_sidebar
show_sidebar()

from src.api_client import (
    get_rooms,
    create_room,
    update_room,
    delete_room
)

rooms = get_rooms()

st.title("🛏️ Rooms")

# OVERVIEW
st.subheader("Overview")
n_cols = 4
for i in range(0, len(rooms), n_cols):
    cols = st.columns(n_cols)
    batch = rooms[i:i + n_cols]
    for j, room in enumerate(batch):
        with cols[j]:
            with st.container(border=True):
                st.markdown(f"**Room {room['room_number']}**")
                st.caption(f"ID: {room['id_room']}")
                st.caption(f"{room['room_type'].title()}")
                st.caption(f"€{room['price_per_night']}/night")
                if room["status"] == "available":
                    st.markdown(":green[● Available]")
                elif room["status"] == "occupied":
                    st.markdown(":red[● Occupied]")
                else:
                    st.markdown(":orange[● Maintenance]")

st.divider()

# CREATE
st.subheader("➕ Create room")

room_number = st.number_input("Room number", min_value=1, step=1)
room_type = st.selectbox("Type", ["single", "double", "suite", "deluxe"])
price_per_night = st.number_input("Price per night (€)", min_value=0.0, step=0.01, value=0.0)
status = st.selectbox("Status", ["available", "occupied", "maintenance"])

if st.button("➕ Create room"):
    with st.spinner("Creating room..."):
        response = create_room({
            "room_number": room_number,
            "room_type": room_type,
            "price_per_night": price_per_night,
            "status": status
        })
    if response.status_code == 200:
        st.success("✅ Room created successfully")
        st.balloons()
    else:
        error_detail = response.json().get("detail", "Unknown error")
        st.error(f"❌ {error_detail}")

st.divider()

# SHOW
st.subheader("📋 Room list")

if st.button("🔍 Show rooms"):
    rooms = get_rooms()
    if rooms:
        df = pd.DataFrame(rooms)
        st.dataframe(df)
    else:
        st.info("ℹ️ No rooms found")

st.divider()

# UPDATE
st.subheader("🔄 Update room")

update_id = st.number_input("Room ID to update", min_value=1, step=1)

col1, col2 = st.columns(2)
with col1:
    new_room_number = st.number_input("New room number", min_value=1, step=1)
    new_price = st.number_input("New price per night (€)", min_value=0.0, step=0.01, value=0.0)
with col2:
    new_room_type = st.selectbox("New type", ["single", "double", "suite", "deluxe"])
    new_status = st.selectbox("New status", ["available", "occupied", "maintenance"])

if st.button("🔄 Update room"):
    with st.spinner("Updating room..."):
        response = update_room(update_id, {
            "room_number": new_room_number,
            "room_type": new_room_type,
            "price_per_night": new_price,
            "status": new_status
        })
    if response.status_code == 200:
        st.success("✅ Room updated successfully")
    else:
        error_detail = response.json().get("detail", "Unknown error")
        st.error(f"❌ {error_detail}")

st.divider()

# DELETE
st.subheader("🗑️ Delete room")

delete_id = st.number_input("Room ID to delete", min_value=1, step=1)

if st.button("🗑️ Delete room"):
    response = delete_room(delete_id)
    if response.status_code == 200:
        st.success("✅ Room deleted successfully")
    else:
        error_detail = response.json().get("detail", "Unknown error")
        st.error(f"❌ {error_detail}")