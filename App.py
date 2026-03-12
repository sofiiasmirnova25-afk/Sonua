import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Hobby Chatbot", page_icon="💬")

st.title("💬 Hobby Chatbot")
st.write("Hi! I'm a chatbot that loves talking about hobbies and interests 😊")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Bot logic
def generate_reply(user_input):

    text = user_input.lower()

    hobbies = [
        "🎸 Learning a musical instrument",
        "📚 Reading books",
        "🏃 Running or jogging",
        "🎨 Drawing or painting",
        "📷 Photography",
        "🎮 Gaming",
        "💻 Coding",
        "🍳 Cooking",
        "🌱 Gardening"
    ]

    if "hello" in text or "hi" in text:
        return "Hello! 👋 Tell me about your hobbies."

    elif "hobby" in text and ("suggest" in text or "idea" in text or "recommend" in text):
        return "Here are some hobby ideas:\n\n" + "\n".join(random.sample(hobbies,3))

    elif "music" in text:
        return "Music is great! 🎵 Do you play an instrument or just listen?"

    elif "sport" in text or "football" in text or "basketball" in text:
        return "Sports are fun! ⚽ Do you prefer playing or watching?"

    elif "read" in text or "book" in text:
        return "Reading is amazing! 📚 What type of books do you enjoy?"

    elif "game" in text or "gaming" in text:
        return "Gaming is fun! 🎮 What games do you like?"

    elif "coding" in text or "programming" in text:
        return "Coding is awesome! 💻 What language do you like?"

    elif "bye" in text:
        return "Goodbye! 👋 Come back if you want to chat about hobbies!"

    else:
        return random.choice([
            "That sounds interesting! Tell me more 😊",
            "Cool! How did you start doing that?",
            "Nice! What do you enjoy most about it?",
            "That sounds fun! Do you do it often?"
        ])


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Tell me about your hobbies...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    reply = generate_reply(user_input)

    # Show bot message
    st.session_state.messages.append({"role":"assistant","content":reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
