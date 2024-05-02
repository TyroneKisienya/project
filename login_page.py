import streamlit as st
import mysql.connector
from passlib.hash import pbkdf2_sha256

def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
    except mysql.connector.Error as e:
        print(e)
    return conn

def authenticate_user(conn, email, password):
    sql_authenticate_user = """
        SELECT * FROM users WHERE email = %s
    """
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_authenticate_user, (email,))
        user = cursor.fetchone()
        if user and pbkdf2_sha256.verify(password, user['password']):
            return user
        else:
            return None
    except mysql.connector.Error as e:
        print(e)
        return None

def login_page():
    st.title("User Login")

    conn = create_connection()

    with st.form("login_form"):
        st.write("Please log in:")
        login_email = st.text_input("Email")
        login_password = st.text_input("Password", type="password")
        login_submitted = st.form_submit_button("Login")

    if login_submitted:
        if login_email and login_password:
            user = authenticate_user(conn, login_email, login_password)
            if user:
                st.success("Login successful! Welcome, {}!".format(user['first_name']))
            else:
                st.error("Login failed. Invalid email or password.")
        else:
            st.warning("Please enter your email and password.")
