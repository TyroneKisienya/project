import streamlit as st

def user_page(user_name):
    st.title("User Page")
    st.write(f"Hello, {user_name}!")
    st.write("This is the user page. You can add more content here.")

    # Redirect to medical data page
    if st.button("View Medical Data"):
        medical_data_page(user_name)

