import streamlit as st
import random

st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Simple Chatbot")
st.write("No API needed 🚀")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

def generate_reply(user_input):
    text = user_input.lower()

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
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = generate_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(reply)
