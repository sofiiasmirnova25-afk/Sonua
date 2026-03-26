import streamlit as st

st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #0e1117;
    }

    /* General text inside main container */
    .stText, .css-1d391kg, .css-1v3fvcr { 
        color: #FF69B4 !important;
    }

    /* Headings */
    h1, h2, h3 {
        color: #FF69B4 !important;
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
        color: #FF69B4;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #FF69B4 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Hello Streamlit")
st.write("This text should now appear pink instead of black.")
st.text_input("Enter something")
st.button("Click Me")
