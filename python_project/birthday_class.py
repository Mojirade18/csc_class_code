class Person:
    populations = 0

    def __init__(self, name, age, gender, DOB, MOB):
        self.name = name
        self.age = age
        self.gender = gender
        self.DOB = DOB
        self.MOB = MOB
        Person.population += 1

    def introduce(self):
        return f"Hey there! my name is {self.name}.\nI am {self.age} years old and identify as {self.gender}."

    def birthday(self):
        self.age += 1
        birth_year = 2025 - self.age
        print(f" Happy Birthday, {self.name}! You are now {self.age} years old.")
        print(f"You were born on {self.DOB}/{self.MOB}/{birth_year}.")

    def is_adult(self):
        if self.age >= 18:
            return " You are an adult."
        else:
            return " You are underaged. Come back when you're 18."

    def greet(self, other_person):
        print(f"{self.name} says: Hi {other_person.name}, nice to meet you!")

    def __str__(self):
        return f"{self.name} - {self.age} years old - Gender: {self.gender}"


# --------- Getting input from the user ---------

print("👤 Let's create a person!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
DOB = int(input("Enter your day of birth (e.g. 14): "))
MOB = int(input("Enter your month of birth (e.g. 3 for March): "))

# Create a person using the input
user_person = Person(name, age, gender, DOB, MOB)

# Try out the methods
print("\n📝 Introduction:")
print(user_person.introduce())

print("\n🎂 Birthday Function:")
user_person.birthday()

print("\n🔞 Age Check:")
print(user_person.is_adult())

print(f"\nTotal people created: {Person.population}")
