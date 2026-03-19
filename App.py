import streamlit as st
import random
import re
from sympy import sympify, simplify, pretty, Add, Mul

st.set_page_config(page_title="Chatbot", page_icon="💬")

st.title("💬 Smart Chatbot")
st.write("Now with math solving 🧠 (step-by-step!)")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Step-by-step math solver
def solve_math(expression):
    try:
        # Only allow numbers and math symbols
        if re.match(r'^[0-9+\-*/().\s]+$', expression):
            expr = sympify(expression)  # Parse safely
            steps = []
            
            # Step 1: show original
            steps.append(f"Original: {expr}")
            
            # Step 2: simplify (this handles distributive/combining like terms)
            simplified_expr = simplify(expr)
            steps.append(f"Simplified: {simplified_expr}")
            
            # Optional: show pretty printing
            pretty_expr = pretty(expr)
            steps.append(f"Pretty form:\n{pretty_expr}")
            
            return "🧮 Step-by-step solution:\n" + "\n".join(steps)
    except Exception as e:
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
        
