import streamlit as st

# Hardcoded credentials (for demo purposes only)
USERNAME = "imdatsing"
PASSWORD = "imdatsing"

def main():
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple authentication logic
        if username == USERNAME and password == PASSWORD:
            st.success("Login successful!")
            # Proceed to the main content of the app
            st.write("Welcome to the main content of the app.")
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
