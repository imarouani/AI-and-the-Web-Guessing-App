import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Welcome",
    page_icon="🌟",
    layout="wide",
)

# Add a background image via inline CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://ibb.co/djY3cSL");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Content placeholder
st.title("Welcome to the App!")
st.write("This is a page with a background image.")
