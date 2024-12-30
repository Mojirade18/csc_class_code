# This a special greeting for the user
print("Hello there this is an information card!")

# This gets the necessary information from the user to run the snippet
print("we would need a little information about you if you dont mind.")
name = str(input("What is your name: "))
age = int(input("How old are you? "))
favourite_color = str(input("What color do you like best? "))
hobby = str(input("What do you like doing best at leisure time? "))

# This prints out useful information to the user
print("Hey " + name + " i like to play with " + str(age) + " years old folks.")
print(f"I also like {hobby} and {favourite_color}.")
print("Hey", name, "i like to play with", age, "years old folks.")