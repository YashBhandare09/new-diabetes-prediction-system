import streamlit as st

# Define the register_admin function
def register_admin(username, password):
    # Your implementation of registering a new admin goes here
    # For demonstration purposes, let's just return True for now
    return True

def admin_signup():
    st.set_page_config(page_title="Admin Signup")
    st.title("Admin Signup")

    # Signup form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Signup button
    if st.button("Signup"):
        # Register new admin
        if register_admin(username, password):
            st.success("Signup successful")
            # Redirect to Admin Panel Page
            st.experimental_rerun()
        else:
            st.error("Username already exists")

if __name__ == "__main__":
    admin_signup()
