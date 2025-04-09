class student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"{self.name} said school is fun."
    
moji_object = student(Moji, 100)
print(moji_object)