# This snippet checks if someone has a in their name and adds the person name to a list
# If the person is not, it should notify the user

print("Hello there!")
print("I trust your day is actively going well")
name = input("Whats your name? ")
lowercase_name = name.lower()
age = int(input("How old are you: "))
gender = input("Are you a boy or a girl")
print("What a beautiful name for a", age, "years old", gender)
list_of_a_students = []
if "a" in lowercase_name:
    list_of_a_students.append(lowercase_name)
    print("You have just been added to the list of those with a in their names.")
    print("Congratulations once again.")
if "a" not in name:
    print("We are so sorry, we can't add you to the list 'try again next year'.")