# This responds to the user's input for any errors too
def chatbot_response(user_input):
    if user_input == "hello":
        return "Hi there! How can I help you?"
    elif user_input == "how are you?":
        return "I'm just a bot, but I'm doing great! How about you?"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."
    
    class ChatBot:
        def __init__(self, name):
            self.name = name
            self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you?": "I'm just a bot, but I'm doing great! How about you?",
            "what is your name?": f"My name is {self.name}.",
            "bye": "Goodbye! Have a great day!"
        }

        def get_response(self, user_input):
            user_input = user_input.lower()
            return self.responses.get(user_input, "Sorry, I don't understand that.")

