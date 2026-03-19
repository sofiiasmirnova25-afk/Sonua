import streamlit as st
import random
import re
from sympy import sympify, simplify, pretty

st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Smart Chatbot")
st.write("Now with math solving 🧠 and hobby suggestions 🎨")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Store last suggested hobby
if "last_hobby" not in st.session_state:
    st.session_state.last_hobby = None

# ✅ Safe step-by-step math solver
def solve_math(expression):
    try:
        # Allow only numbers and math symbols
        if re.match(r'^[0-9+\-*/().\s]+$', expression):
            expr = sympify(expression)
            simplified_expr = simplify(expr)
            steps = f"Step-by-step:\nOriginal: {expr}\nSimplified: {simplified_expr}"
            return f"🧮 Answer:\n{steps}"
    except:
        return None
    return None

# 🎯 Hobbies list
hobbies = [
    "🎸 Try learning guitar!",
    "🎨 Try drawing!",
    "📚 Try reading books!",
    "🏊‍♂️ Try swimming!",
    "🎮 Try gaming!",
    "📝 Try journaling!"
]

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
        hobby = random.choice(hobbies)
        st.session_state.last_hobby = hobby
        return hobby

    elif "another one" in text:
        # Suggest a different hobby
        remaining_hobbies = [h for h in hobbies if h != st.session_state.last_hobby]
        if remaining_hobbies:
            hobby = random.choice(remaining_hobbies)
            st.session_state.last_hobby = hobby
            return hobby
        else:
            return "You've tried all my suggestions! 😅"

    elif "bye" in text:
        return "Goodbye! 👋"

    else:
        return random.choice([
            "Tell me more 🙂",
            "That sounds fun!",
            "Interesting!"
        ])

# Show chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type message or math (e.g. 2+2)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = generate_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(reply)
        
