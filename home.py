import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Guess the Historical Figure",
    page_icon="🎭",
    layout="wide",
)

# CSS for the background and play button
st.markdown(
    """
    <style>
    /* Full-page background */
    .main {
        background-image: url('background.jpg');
        background-size: cover;
        background-position: center;
        height: 100vh;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* Text container styling */
    .content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
        height: 100vh;
    }

    /* Play button styling */
    .play-button {
        font-size: 1.5rem;
        padding: 0.8rem 2rem;
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .play-button:hover {
        background-color: #ff3333;
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render the background
st.markdown('<div class="main"></div>', unsafe_allow_html=True)

# Centered content and button
st.markdown(
    """
    <div class="content">
        <h1 style="color: white; font-size: 3rem; text-shadow: 2px 2px 10px rgba(0,0,0,0.7);">
            Welcome to Guess the Historical Figure
        </h1>
        <p style="color: white; font-size: 1.2rem; text-shadow: 1px 1px 5px rgba(0,0,0,0.5);">
            Test your knowledge and learn about history!
        </p>
        <button class="play-button" onclick="location.href='play_page'">Play</button>
    </div>
    """,
    unsafe_allow_html=True,
)
