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




greeting_message()
while True:
    options()
    intake = input("What have you chosen? ")
    if intake in [1, 2, 3, 4]:
        pass
    else:
        print("Wrong input. Please only input numbers between 1-4")
        continue
    
    if intake == 1:
        sign = input("pick your sign (rock/ paper/ scissors): ").strip().lower()
        