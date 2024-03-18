import streamlit as st

def user_signup():
    st.set_page_config(page_title="User Signup")
    st.title("User Signup")

    # Signup form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Signup button
    if st.button("Signup"):
        # Register new user (you'll implement this)
        if register_user(username, password):
            st.success("Signup successful")
            # Redirect to Diabetes Prediction Form Page
            st.experimental_rerun()
        else:
            st.error("Username already exists")

if __name__ == "__main__":
    user_signup()
