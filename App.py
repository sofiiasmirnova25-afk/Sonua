import streamlit as st

st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: black;
        color: #FF69B4;
    }

    /* General text */
    p, span, div, label {
        color: #FF69B4 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #FF69B4 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: black;
        color: #FF69B4;
        border: 1px solid #FF69B4;
        border-radius: 10px;
    }

    .stButton > button:hover {
        background-color: #FF69B4;
        color: black;
    }

    /* Text inputs and text areas */
    input, textarea {
        background-color: black !important;
        color: #FF69B4 !important;
        border: 1px solid #FF69B4 !important;
    }

    /* Sliders */
    .stSlider div {
        color: #FF69B4 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
