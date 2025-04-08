def chatbot_response(user_input):
    if user_input == "hello":
        return "Hi there! How can I help you?"
    elif user_input == "how are you?":
        return "I'm just a bot, but I'm doing great! How about you?"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."
