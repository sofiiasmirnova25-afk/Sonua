import streamlit as st
import random
import re

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Hobby App", page_icon="🌸")

# ------------------ STYLE ------------------
st.markdown("""
<style>
body, .stApp {
    background-color: #FFF0F5;
}
h1, h2, h3 {
    color: #FF8FB1;
}
.stButton>button {
    background-color: #FF8FB1;
    color: white;
    border-radius: 10px;
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

    st.subheader("Your Preferences")

    creative = st.slider("Creative", 1, 5, 3)
    outdoor = st.slider("Outdoor", 1, 5, 3)
    social = st.slider("Social", 1, 5, 3)
    physical = st.slider("Physical", 1, 5, 3)

    user_text = st.text_area("Extra interests")

    def suggest():
        hobbies = []

        if creative >= 4:
            hobbies += ["🎨 Painting", "✏️ Drawing"]

        if outdoor >= 4:
            hobbies += ["🥾 Hiking"]

        if social >= 4:
            hobbies += ["⚽ Team Sports"]
        elif social <= 2:
            hobbies += ["📚 Reading"]

        if physical >= 4:
            hobbies += ["🏋️ Gym"] if fitness != "Low" else ["🚶 Walking"]

        if "cook" in user_text.lower():
            hobbies.append("👩‍🍳 Cooking")

        return hobbies

    if st.button("✨ Suggest"):
        results = suggest()
        if results:
            for h in results:
                st.write(h)
        else:
            st.write("Try adjusting your answers 🌸")

# =====================================================
# ================= CHATBOT ============================
# =====================================================
with tab2:

    st.title("💬 Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    hobbies = [
        "🎸 Try guitar!",
        "🎨 Try drawing!",
        "📚 Try reading!",
        "🎮 Try gaming!"
    ]

    def solve_math(expr):
        try:
            if not re.match(r'^[0-9+\-*/().\s]+$', expr):
                return None
            return f"Answer: {eval(expr)}"
        except:
            return None

    def reply(user):
        text = user.lower()

        math = solve_math(text)
        if math:
            return math

        if "hi" in text:
            return "Hello 🌸"

        if "hobby" in text:
            return random.choice(hobbies)

        if "bye" in text:
            return "Bye 💕"

        return "Tell me more 😊"

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Type here...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = reply(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            st.write(response)
