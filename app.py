import streamlit as st
from register_page import registration_page
from login_page import login_page
from user_page import user_page
from med_page import medical_data_page

def main():
    st.set_page_config(layout="wide")
    st.title("Welcome to the App")

    # Show login page initially
    login_page()

    # Redirect to registration page
    if st.button("Register"):
        registration_page()

if __name__ == "__main__":
    main()

