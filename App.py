import streamlit as st

# App title
st.set_page_config(page_title="Hobby Chatbot", page_icon="💬")
st.title("💬 Interests & Hobbies Chatbot")

st.write("Hi! I'm a chatbot that loves talking about interests and hobbies 😁")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Simple function to generate a reply locally
def generate_reply(user_input):
    user_input = user_input.lower()
    if "music" in user_input:
        return "I love music too! What's your favorite genre?"
    elif "sports" in user_input:
        return "Sports are fun! Do you like playing or watching?"
    elif "reading" in user_input:
        return "Reading is amazing! Who's your favorite author?"
    elif "coding" in user_input or "programming" in user_input:
        return "Coding is exciting! What languages do you like?"
    else:
        return "That sounds interesting! Tell me more."

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Tell me about your hobbies or interests...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate bot reply
    reply = generate_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    # Display the reply
    with st.chat_message("assistant"):
        st.markdown(reply)
