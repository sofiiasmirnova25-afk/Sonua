import streamlit as st
import random

# Page configuration
st.set_page_config(
    page_title="Hobby Chatbot",
    page_icon="💬",
    layout="centered"
)

# Title
st.title("💬 Hobby Chatbot")
st.write("Hi! I'm a chatbot that loves talking about hobbies and interests 😄")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chatbot reply function (no API)
def generate_reply(user_input):

    text = user_input.lower()

    music_responses = [
        "I love music too! 🎵 What's your favorite genre?",
        "Music is amazing! Do you play any instruments?",
        "Nice! Who is your favorite artist?"
    ]

    sports_responses = [
        "Sports are fun! ⚽ Do you like playing or watching?",
        "Cool! What is your favorite team?",
        "Nice! Do you play any sports yourself?"
    ]

    reading_responses = [
        "Reading is awesome 📚 What kind of books do you like?",
        "Who's your favorite author?",
        "Do you prefer fiction or non-fiction?"
    ]

    coding_responses = [
        "Coding is exciting 💻 What language do you like?",
        "Nice! Are you building any projects?",
        "Programming is fun! Do you like Python?"
    ]

    gaming_responses = [
        "Gaming is fun 🎮 What games do you play?",
        "Do you prefer PC, console, or mobile games?",
        "Multiplayer or single-player games?"
    ]

    if "music" in text:
        return random.choice(music_responses)

    elif "sport" in text or "football" in text or "basketball" in text:
        return random.choice(sports_responses)

    elif "read" in text or "book" in text:
        return random.choice(reading_responses)

    elif "coding" in text or "programming" in text or "python" in text:
        return random.choice(coding_responses)

    elif "game" in text or "gaming" in text:
        return random.choice(gaming_responses)

    elif "hello" in text or "hi" in text:
        return "Hello! 👋 Tell me about your hobbies."

    elif "bye" in text:
        return "Goodbye! 👋 It was nice chatting with you."

    else:
        return random.choice([
            "That sounds interesting! Tell me more 😊",
            "Cool! What do you like most about it?",
            "Nice! How long have you been interested in that?",
            "That's awesome! What got you into it?"
        ])


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_input = st.chat_input("Tell me about your hobbies...")

if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate reply
    reply = generate_reply(user_input)

    # Save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)
