import streamlit as st

st.set_page_config(
    page_title="Hotel Booking System",
    layout="wide"
)

st.title("Hotel Booking System")

st.markdown("""
Welcome to the hotel management platform

Choose an option:
""")

st.page_link("pages/1_Guests.py",label=" Guests")
st.page_link("pages/2_Rooms.py", label="Rooms")
st.page_link("pages/3_Bookings.py", label="Bookings")
st.page_link("pages/4_Dashboard.py", label="Dashboards")

