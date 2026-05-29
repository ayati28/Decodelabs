responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "hey": "Hey! What's up?",
    "how are you": "I'm doing great! Thanks for asking. 😄",
    "your name": "I'm Ayati's AI Chatbot 🤖",
    "who are you": "I'm a simple rule-based chatbot.",
    "help": "You can ask me about my name, greeting, or how I'm doing.",
    "bye": "Goodbye! Have a great day! 👋"
}

print("🤖 Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    user_input = user_input.replace("?", "")
    user_input = user_input.replace("!", "")
    user_input = user_input.replace(".", "")

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break

    found = False

    for key in responses:
        if key in user_input:
            print("Bot:", responses[key])
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't understand that yet. 😅")