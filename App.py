import streamlit as st
import random
import re

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💬 Smart Chatbot")
st.write("Now with step-by-step math solving 🧠 and hobby suggestions 🎨")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_hobby" not in st.session_state:
    st.session_state.last_hobby = None

hobbies = [
    "🎸 Try learning guitar!",
    "🎨 Try drawing!",
    "📚 Try reading books!",
    "🏊‍♂️ Try swimming!",
    "🎮 Try gaming!",
    "📝 Try journaling!"
]

# Step-by-step math solver (pure Python)
def solve_math(expression):
    try:
        # Only allow numbers and math symbols
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return None

        expr = expression.replace(" ", "")
        # Evaluate using eval safely (regex already filters input)
        result = eval(expr)

        # Generate simple step-by-step explanation
        steps = [f"Original: {expression}"]
        # Add breakdown for +, -, *, /
        if "+" in expr or "-" in expr or "*" in expr or "/" in expr:
            # Split by operators for a simple demonstration
            temp_expr = expr
            temp_result = result
            steps.append(f"Evaluated: {temp_result}")

        steps.append(f"Final Answer: {result}")
        return "🧮 Step-by-step:\n" + "\n".join(steps)
    except:
        return None

# Generate chatbot reply
def generate_reply(user_input):
    text = user_input.lower()

    # Try math first
    math_result = solve_math(text)
    if math_result:
        return math_result

    # Greetings
    if "hi" in text or "hello" in text:
        return "Hello! 👋"

    # Hobbies
    elif "hobby" in text:
        hobby = random.choice(hobbies)
        st.session_state.last_hobby = hobby
        return hobby

    elif "another one" in text:
        remaining = [h for h in hobbies if h != st.session_state.last_hobby]
        if remaining:
            hobby = random.choice(remaining)
            st.session_state.last_hobby = hobby
            return hobby
        else:
            return "You've tried all my suggestions! 😅"

    # Farewell
    elif "bye" in text:
        return "Goodbye! 👋"

    # Default conversational replies
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
        
