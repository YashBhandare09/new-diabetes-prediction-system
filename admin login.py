import streamlit as st

def admin_login():
    st.set_page_config(page_title="Admin Login")
    st.title("Admin Login")

    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        # Authenticate user (you'll implement this)
        if authenticate_admin(username, password):
            st.success("Login successful")
            # Redirect to Admin Panel Page
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    admin_login()
