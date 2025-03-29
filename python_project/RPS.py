import random
def greeting_message():
    message = """Are you bored?
    If yes then you are at the right place
    If no then trust me you are still at the right place 
    Let the fun begin
    """
    print(message)

def options():
    option = """What do you want to do
    1. play rock, paper and scissors
    2. replay match
    3. show scores
    4. exit game"""
    print(option)

        


mylist = ["rock", "paper", "scissors"]



user_score = 0
computer_score = 0
greeting_message()
while True:
    options()
    intake = int(input("What have you chosen?(1-4) "))
    if intake in [1, 2, 3, 4]:
        pass
    else:
        print("Wrong input. Please only input numbers between 1-4")
        continue
    
    if intake == 1:
        sign = input("pick your sign (rock/ paper/ scissors): ").strip().lower()
        random_int = random.randrange(0, 2)
        computer_sign = mylist[random_int]

        if sign == "rock" and computer_sign == "scissors":
            print(f"I pick {computer_sign}")
            print("You win")
            user_score += 1
            print(f"scores: you {user_score} - me {computer_score}")
        elif sign == "rock" and computer_sign == "paper":
            print(f"I pick {computer_sign}")
            computer_score += 1
            print("I won")
            print(f"scores: you {user_score} - me {computer_score}")
        elif sign == "paper" and computer_sign == "rock":
            print(f"I pick {computer_sign}")
            print("You win")
            user_score += 1
            print(f"scores: you {user_score} - me {computer_score}")
        elif sign == "paper" and computer_sign == "scissors":
            print(f"I pick {computer_sign}")
            computer_score += 1
            print("I won")
            print(f"scores: you {user_score} - me {computer_score}")
        elif sign == "scissors" and computer_sign == "rock":
            print(f"I pick {computer_sign}")
            computer_score += 1
            print("I won")
            print(f"scores: you {user_score} - me {computer_score}")
        elif sign == "scissors" and computer_sign == "paper":
            print(f"I pick {computer_sign}")
            print("You win")
            user_score += 1
            print(f"scores: you {user_score} - me {computer_score}")
        else:
            print("Incorrect input!")