import json
import os

class ChatBot:
    def __init__(self, name, memory_file="chatbot_memory.json"):
        self.name = name
        self.memory_file = memory_file
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you?": "I'm just a bot, but I'm doing great! How about you?",
            "what's your name?": f"My name is {self.name}.",
            "bye": "Goodbye! Have a great day!"
        }
        self.load_memory()

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        return self.responses.get(user_input)

    def learn_response(self, user_input, new_response):
        self.responses[user_input.lower().strip()] = new_response
        self.save_memory()

    def save_memory(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.responses, file)

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.responses.update(json.load(file))

def start_chat():
    bot = ChatBot("Chatter")
    print("🤖 Chatter: Hello! Start chatting with me. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print(f"🤖 {bot.name}: {bot.get_response('bye')}")
            break

        response = bot.get_response(user_input)
        if response:
            print(f"🤖 {bot.name}: {response}")
        else:
            print(f"🤖 {bot.name}: I don't understand that.")
            teach = input("Would you like to teach me how to respond to that? (yes/no): ").lower().strip()
            if teach == "yes":
                new_reply = input("What should I say when you say that? ")
                bot.learn_response(user_input, new_reply)
                print(f"🤖 {bot.name}: Got it! I'll remember that.")

# Start the chatbot
start_chat()
