import streamlit as st

st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #0e1117;
    }

    /* Main text */
    p, span, div, label {
        color: #FF69B4;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FF69B4;
    }

    /* Buttons */
    .stButton > button {
        background-color: transparent;
        color: #FF69B4;
        border: 1px solid #FF69B4;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }

    .stButton > button:hover {
        background-color: #FF69B4;
        color: black;
    }

    /* Input fields */
    .stTextInput input, .stTextArea textarea {
        background-color: #1c1f26;
        color: #FF69B4;
        border: 1px solid #FF69B4;
        border-radius: 6px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111;
    }
    </style>
    """,
    unsafe_allow_html=True
)
