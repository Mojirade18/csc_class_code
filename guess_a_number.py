import random
# This snippet alllows the user select a nmber and the  computer does the same thing ie gets the same value. he or she guessed right
print("You are welcome to our gaming world!")
print("Would you like to think of a nmber?")
random_number = random.randint(1, 100)
while True:
        try:
            user_number = int(input("Guess a value: "))
            if user_number < random_number:
                print("Your number is smaller than mine")
                print("Pick another number.")
            elif user_number > random_number:
                 print("Your number is greater than mine.")
                 print ("Pick another number.")
            else:
                 print(f"Weldone you picked {random_number}")
                 break
        except ValueError:
             print("Please put in the right figure")
print('Weldon, you are good at guessing.')             