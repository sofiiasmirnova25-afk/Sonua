
def generate_reply(user_input):

    math_result = solve_math(user_input)
    if math_result:
        return math_result

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
