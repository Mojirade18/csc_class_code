import random
Greeting_message = """Hello welcome to message coder.
This encrypt your message to your friends.
Enjoy the ride!"""
print(Greeting_message)
print("What do you want to do?")
print("1. encrypt your message.")
#print("2. De-encrypt your message.")
choice = int(input("What is your choice 1/2: "))
encrypted_value = ""

if choice == 1:
    word = input("Type in the word you want to encrypt: ")
    for a in word:
        if a.isalpha():
            a = random.randrange(1,100)
            encrypted_value += str(a)

print(f"The encrypted numbers for the word {word} is {encrypted_value}")
            