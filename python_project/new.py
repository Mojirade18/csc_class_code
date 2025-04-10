class person(): 
    def __init__(self, name, age, gender, DOB ):
        self.name = name
        self.age = age
        self.gender = gender
        self.DOB = DOB
    
    def introduce(self):
        return f"Hey there my name is {self.name}\ni am {self.age} years old."
    def birthday(self):
        print(f"Since i am {self.age}, then you should probably get my age right")
        print(f"I was born {2025 - self.age}")
        print("Therefore my birthday is ")