import streamlit as st
from pathlib import Path

def set_background(image_file):
    """
    Sets the background image for the Streamlit app.
    :param image_file: Path to the local background image.
    """
    # Resolve the absolute path of the image file
    image_path = Path(image_file).resolve()
    css = f"""
    <style>
    .stApp {{
        background: url('file://{image_path}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
