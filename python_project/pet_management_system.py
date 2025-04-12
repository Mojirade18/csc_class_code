# 🐶 Base class (Parent)
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} has been fed. Hunger: {self.hunger}")

    def speak(self):
        print(f"{self.name} makes a sound.")

# 🐕 Dog class inherits from Pet
class Dog(Pet):
    def speak(self):
        print(f"{self.name} says Woof!")

# 🐱 Cat class inherits from Pet
class Cat(Pet):
    def speak(self):
        print(f"{self.name} says Meow!")

# 🐦 Bird class inherits from Pet
class Bird(Pet):
    def speak(self):
        print(f"{self.name} says Tweet!")

# 🧪 Let's test it
def main():
    # Create one pet of each type
    dog = Dog("Max")
    cat = Cat("Luna")
    bird = Bird("Kiwi")

    # Call their methods
    dog.speak()
    cat.speak()
    bird.speak()

    # Feed the dog
    dog.feed()
    dog.feed()

main()
