import streamlit as st
import pandas as pd
from src.sidebar import show_sidebar
show_sidebar()
from src.api_client import (
    get_guests,
    create_guest,
    update_guest,
    delete_guest
)

st.title("🏨 Guests")

#cREAT
st.subheader("➕ Create guest")

col1, col2 = st.columns(2)
with col1:
    first_name = st.text_input("👤First name")
    email = st.text_input("📧Email")
    dni = st.text_input("🆔DNI")
with col2:
    last_name = st.text_input("👤Last name")
    phone = st.text_input("📞Phone")

if st.button("➕ Create guest"):
    with st.spinner("Creating guest..."):
        response = create_guest({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "dni": dni
        })
    if response.status_code == 200:
        st.success("Guest created successfully")
        st.balloons()
    else:
        st.error("Error creating guest")


st.divider()


# SHOW 
st.subheader(" 📋 Guest list")

if st.button(" 🔍 Show guests"):

    guests = get_guests()

    if guests:

        df = pd.DataFrame(guests)

        st.dataframe(df)

    else:
        st.info(" ℹ️ No guests found")


st.divider()

#UPDATE
st.subheader("  🔄 Update guest")

update_id = st.number_input(
    "Guest ID to update",
    min_value=1,
    step=1
)

col1, col2 = st.columns(2)
with col1:
    new_first_name = st.text_input("New first name")
    new_email = st.text_input("New email")
    new_dni = st.text_input("New DNI")
with col2:
    new_last_name = st.text_input("New last name")
    new_phone = st.text_input("New phone")

if st.button("Update guest"):
    response = update_guest(
        update_id,
        {
            "first_name": new_first_name,
            "last_name": new_last_name,
            "email": new_email,
            "phone": new_phone,
            "dni": new_dni
        }
    )
    if response.status_code == 200:
        st.success("Guest updated")

    else:
        st.error("Error updating guest")


st.divider()


# DELETE
st.subheader("❌ Delete guest")

delete_id = st.number_input(
    "Guest ID to delete",
    min_value=1,
    step=1
)

if st.button("❌ Delete guest"):

    response = delete_guest(delete_id)

    if response.status_code == 200:
        st.success("Guest deleted")

    else:
        st.error("Error deleting guest")
        