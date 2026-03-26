import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
from PIL import Image
import random
import re

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Hobby Finder + Chatbot",
    page_icon="🌸",
    layout="centered"
)

# ------------------ PASTEL THEME ------------------
st.markdown("""
<style>
:root {
    --main-bg: #FFF0F5;
    --secondary-bg: #FFE4EC;
    --accent: #FF8FB1;
    --text: #4A4A4A;
}

body, .stApp {
    background-color: var(--main-bg);
    color: var(--text);
}

.stButton>button {
    background-color: var(--accent);
    color: white;
    border-radius: 12px;
    border: none;
}

.stButton>button:hover {
    background-color: #ff6f9f;
}

h1, h2, h3 {
    color: var(--accent);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TABS ------------------
tab1, tab2 = st.tabs(["🎯 Hobby Finder", "💬 Chatbot"])

# =====================================================
# ================= HOBBY FINDER =======================
# =====================================================
with tab1:

    st.title("🎨 Find Your Hobby")

    age = st.number_input("Age", 5, 100, 20)
    fitness = st.selectbox("Fitness Level", ["Low", "Medium", "High"])

    questions = {
        "creative": "Creative",
        "outdoor": "Outdoor",
        "social": "Social",
        "physical": "Physical",
        "learning": "Learning",
        "technology": "Technology",
        "music": "Music",
        "patience": "Patience",
    }

    answers = {k: st.slider(v, 1, 5, 3) for k, v in questions.items()}

    user_text = st.text_area("Extra interests")

    # -------- SMART SCORING SYSTEM --------
    hobby_db = {
        "🎨 Painting": {"creative":5, "patience":4},
        "💻 Coding": {"technology":5, "learning":4},
        "🏋️ Gym": {"physical":5},
        "📚 Reading": {"learning":5, "patience":4},
        "⚽ Football": {"physical":5, "social":4},
        "🎤 Singing": {"music":5, "social":3},
        "🥾 Hiking": {"outdoor":5},
        "🧘 Yoga": {"physical":3, "patience":5},
    }

    def score_hobbies():
        scores = {}

        for hobby, traits in hobby_db.items():
            score = 0
            for t, weight in traits.items():
                score += answers[t] * weight
            scores[hobby] = score

        sorted_hobbies = sorted(scores, key=scores.get, reverse=True)

        # text boost
        if "cook" in user_text.lower():
            sorted_hobbies.insert(0, "👩‍🍳 Cooking")

        return list(OrderedDict.fromkeys(sorted_hobbies[:6]))

    def radar_chart():
        labels = list(answers.keys())
        values = [v/5 for v in answers.values()]

        values += values[:1]
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]

        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        fig.patch.set_facecolor("#FFF0F5")
        ax.set_facecolor("#FFE4EC")

        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        return fig

    if st.button("✨ Suggest"):
        st.pyplot(radar_chart())
        for h in score_hobbies():
            st.write(h)

# =====================================================
# ================= CHATBOT ============================
# =====================================================
with tab2:

    st.title("💬 Smart Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "last_hobby" not in st.session_state:
        st.session_state.last_hobby = None

    hobbies = [
        "🎸 Try guitar!",
        "🎨 Try drawing!",
        "📚 Try reading!",
        "🏊 Try swimming!",
        "🎮 Try gaming!"
    ]

    # -------- BETTER MATH SOLVER --------
    def solve_math(expr):
        try:
            if not re.match(r'^[0-9+\-*/().\s]+$', expr):
                return None

            expr = expr.replace(" ", "")
            result = eval(expr)

            steps = []
            steps.append(f"Expression: {expr}")

            if "*" in expr:
                steps.append("Step: Multiplication first")

            if "/" in expr:
                steps.append("Step: Division")

            if "+" in expr or "-" in expr:
                steps.append("Step: Addition/Subtraction")

            steps.append(f"Final Answer = {result}")

            return "\n".join(steps)

        except:
            return None

    # -------- SMART RULE-BASED CHAT --------
    def chatbot(user):
        text = user.lower()

        # math
        math = solve_math(text)
        if math:
            return "🧮\n" + math

        # greetings
        if any(w in text for w in ["hi","hello","hey"]):
            return random.choice([
                "Hey there 🌸",
                "Hello 😊",
                "Hi! How can I help?"
            ])

        # mood detection
        if "sad" in text:
            return "I'm here for you 💗 Maybe try a relaxing hobby?"

        # hobbies
        if "hobby" in text:
            h = random.choice(hobbies)
            st.session_state.last_hobby = h
            return h

        if "another" in text:
            remaining = [h for h in hobbies if h != st.session_state.last_hobby]
            return random.choice(remaining) if remaining else "That's all I got 😅"

        # fallback
        return random.choice([
            "Tell me more 😊",
            "Interesting 👀",
            "That sounds fun 🌸"
        ])

    # display messages
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    user_input = st.chat_input("Type message or math (e.g. 3*5+2)")

    if user_input:
        st.session_state.messages.append({"role":"user","content":user_input})

        reply = chatbot(user_input)

        st.session_state.messages.append({"role":"assistant","content":reply})

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            st.write(reply)
