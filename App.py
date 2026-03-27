import streamlit as st
import random
import re

st.set_page_config(page_title="Chatbot", page_icon="💬")

# 🎨 FIXED GLOBAL STYLING
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #0e1117;
        color: #FF69B4;
    }

    /* Force ALL text pink */
    * {
        color: #FF69B4 !important;
    }

    /* Chat bubbles */
    [data-testid="stChatMessage"] {
        background-color: #1c1f26;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* User vs assistant */
    [data-testid="stChatMessage"][data-testid*="user"] {
        border: 1px solid #FF69B4;
    }

    [data-testid="stChatMessage"][data-testid*="assistant"] {
        border: 1px solid #FF69B4;
    }

    /* Chat input box */
    [data-testid="stChatInput"] textarea {
        background-color: #1c1f26 !important;
        color: #FF69B4 !important;
        border: 1px solid #FF69B4 !important;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton > button {
        background-color: transparent;
        color: #FF69B4;
        border: 1px solid #FF69B4;
        border-radius: 8px;
    }

    .stButton > button:hover {
        background-color: #FF69B4;
        color: black;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💬 Smart Chatbot")
st.write("Now with math solving 🧠")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Safe math solver
def solve_math(expression):
    try:
        if re.match(r'^[0-9+\-*/().\s]+$', expression):
            result = eval(expression)
            return f"🧮 Answer: {result}"
    except:
        return None
    return None

# Chatbot logic
def generate_reply(user_input):
    text = user_input.lower()

    # 🔢 Try math first
    math_result = solve_math(text)
    if math_result:
        return math_result

    # 🎯 Normal chatbot
    if "hi" in text or "hello" in text:
        return "Hello! 👋"

    elif "hobby" in text:
        return random.choice([
            "🎸 Try learning guitar!",
            "🎨 Try drawing!",
            "📚 Try reading books!"
        ])

    elif "bye" in text:
        return "Goodbye! 👋"

    else:
        return random.choice([
            "Tell me more 🙂",
            "That sounds fun!",
            "Interesting!"
        ])

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type message or math (e.g. 2+2)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = generate_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(reply)
