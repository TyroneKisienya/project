import streamlit as st

def medical_data_page(full_name=None):
    st.title("Medical Data")

    st.write("Please fill out the medical data:")

    if full_name:
        st.write(f"Full Name: {full_name}")

    # If imported data, display relevant information
    if full_name:
        st.write("Data imported from hospital.")
    # If creating new data, capture full name and ask for additional information
    else:
        st.write("Creating new data.")
        st.write("Additional information required:")
        # Placeholder for form inputs
        additional_info = st.text_input("Additional Information")
        if st.button("Save"):
            # Process the additional information here
            st.success("Additional information saved successfully.")

