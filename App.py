import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Hobby Chatbot", page_icon="💬")

st.title("💬 Hobby Chatbot")
st.write("Chat with a simple bot — no API needed!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chatbot logic
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
        return "Here are some hobby ideas:\n\n" + "\n".join(random.sample(hobbies, 3))

    elif "music" in text:
        return "Music is great! 🎵 Do you play or just listen?"

    elif "sport" in text or "football" in text or "basketball" in text:
        return "Sports are fun! ⚽ Do you like playing or watching?"

    elif "read" in text or "book" in text:
        return "Reading is awesome! 📚 What do you like to read?"

    elif "game" in text:
        return "Gaming is fun! 🎮 What games do you play?"

    elif "coding" in text or "programming" in text:
        return "Coding is cool! 💻 What language do you use?"

    elif "bye" in text:
        return "Goodbye! 👋 Come back anytime!"

    else:
        return random.choice([
            "That sounds interesting! 😊",
            "Tell me more!",
            "Nice! What do you enjoy most?",
            "Sounds fun! Do you do it often?"
        ])

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    response = generate_reply(user_input)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display messages
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        st.markdown(response)
