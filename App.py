import streamlit as st

# App title
st.set_page_config(page_title="Hobby Chatbot", page_icon="💬")
st.title("💬 Interests & Hobbies Chatbot")

st.write("Hi! I'm a chatbot that loves talking about interests and hobbies 😄")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Tell me about your hobbies or interests...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Simple chatbot logic
    user_text = user_input.lower()

    if "music" in user_text:
        response = "🎵 Nice! What kind of music do you enjoy?"
    elif "sport" in user_text or "sports" in user_text:
        response = "🏅 Sports are awesome! Do you play or just watch?"
    elif "reading" in user_text or "books" in user_text:
        response = "📚 Reading is a great hobby! What’s your favorite genre?"
    elif "gaming" in user_text or "games" in user_text:
        response = "🎮 Cool! What games are you into?"
    elif "art" in user_text or "drawing" in user_text:
        response = "🎨 That’s creative! What kind of art do you like making?"
    else:
        response = "😄 That sounds interesting! Tell me more about it."

    # Show bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
