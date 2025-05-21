import random

def greeting_message():
    message = """Are you bored or stressed OR HAPPY?
    If yes, then you are at the right place.
    If no, then trust me, you are still at the right place.
    Let the fun begin!
    """
    print(message)

def options():
    option = """What do you want to do?
    1. Play Rock, Paper, Scissors
    2. Exit game
    """
    print(option)

mylist = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

greeting_message()
options()

# Ensure valid input for menu selection
while True:
    intake = input("What have you chosen? (1/2): ").strip()
    if intake in ["1", "2"]:
        intake = int(intake)
        break
    print("Wrong input. Please only input numbers 1 or 2.")

if intake == 1:
    # Ensure valid input for number of rounds
    while True:
        rounds = input("How many rounds do you want to do? ").strip()
        if rounds.isdigit() and int(rounds) > 0:
            rounds = int(rounds)
            break
        print("Please enter a valid positive number!")
# A loop to make sure if loops through a certain number of rounds called by the user
    for i in range(rounds):
        # Get user input and ensure it's valid
        while True:
            sign = input("Pick your sign (rock/paper/scissors): ").strip().lower()
            if sign in mylist:
                break
            print("Invalid input! Please choose rock, paper, or scissors.")

        # Computer randomly selects a sign
        computer_sign = random.choice(mylist)
        print(f"I pick {computer_sign}")

        # Determine the winner
        if sign == computer_sign:
            print("This is a draw.")
        elif (sign == "rock" and computer_sign == "scissors") or \
             (sign == "paper" and computer_sign == "rock") or \
             (sign == "scissors" and computer_sign == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("I won!")
            computer_score += 1

        # Display current scores
        print(f"Scores: You {user_score} - Me {computer_score}\n")

    # Display final results
    print("Final Scores:")
    print(f"You: {user_score}, Me: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner! 🎉")
    elif user_score < computer_score:
        print("I win this time! Better luck next time. 😈")
    else:
        print("It's a tie! Well played. 🤝")

elif intake == 2:
    print("Thank you for playing! See you next time.")
    exit()
