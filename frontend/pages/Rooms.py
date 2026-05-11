import streamlit as st
import pandas as pd

from src.api_client import (
    get_rooms,
    get_room,
    create_room,
    update_room,
    delete_room
)

st.title("Rooms")


# CREATE
st.subheader("Create room")

number = st.number_input("Room number", min_value=1, step=1)
room_type = st.selectbox("Type", ["single", "double", "suite", "deluxe"])
base_price = st.number_input("Price per night (€)", min_value=0.0, step=0.01)
capacity = st.number_input("Capacity", min_value=1, step=1)
description = st.text_area("Description")
available = st.checkbox("Available", value=True)

if st.button("Create room"):
    response = create_room({
        "number": number,
        "type": room_type,
        "base_price": base_price,
        "capacity": capacity,
        "description": description,
        "available": available
    })

    if response.status_code == 200:
        st.success("Room created successfully")
    else:
        st.error(f"Error creating room: {response.status_code}")


st.divider()


# SHOW
st.subheader("Room list")

if st.button("Show rooms"):
    rooms = get_rooms()

    if rooms:
        df = pd.DataFrame(rooms)
        st.dataframe(df)
    else:
        st.info("No rooms found")


st.divider()


# UPDATE
st.subheader("Update room")

update_id = st.number_input("Room ID to update", min_value=1, step=1)
new_number = st.number_input("New room number", min_value=1, step=1)
new_type = st.selectbox("New type", ["single", "double", "suite"])
new_base_price = st.number_input("New price per night (€)", min_value=0.0, step=1)
new_capacity = st.number_input("New capacity", min_value=1, step=1)
new_description = st.text_area("New description")
new_available = st.checkbox("Available ", value=True)

if st.button("Update room"):
    response = update_room(update_id, {
        "number": new_number,
        "type": new_type,
        "base_price": new_base_price,
        "capacity": new_capacity,
        "description": new_description,
        "available": new_available
    })

    if response.status_code == 200:
        st.success("Room updated successfully")
    else:
        st.error(f"Error updating room: {response.status_code}")


st.divider()


# DELETE
st.subheader("Delete room")

delete_id = st.number_input("Room ID to delete", min_value=1, step=1)

if st.button("Delete room"):
    response = delete_room(delete_id)

    if response.status_code == 200:
        st.success("Room deleted successfully")
    else:
        st.error(f"Error deleting room: {response.status_code}")