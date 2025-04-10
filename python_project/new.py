class person(): 
    def __init__(self, name, age, gender, DOB, MOB ):
        self.name = name
        self.age = age
        self.gender = gender
        self.DOB = DOB
        self.MOB = MOB
    
    def introduce(self):
        return f"Hey there my name is {self.name}\ni am {self.age} years old."
    def birthday(self):
        print(f"Since i am {self.age}, then you should probably get my age right")
        print(f"I was born {2025 - self.age}")
        print(f"Therefore my birthday is {self.DOB} -  {self.MOB} - {2025 - self.age}")
    def adult(self):
        if self.age >= 18:
            print("You are an adult.")
        else:
            print("You are underaged. Come back when you have clocked 18.")

person1 = person("Ada", 25, "female", 14, 3)
person2 = person("Zik", 15, "male", 7, 10)