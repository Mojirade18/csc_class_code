class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} said school is fun."

class Moji(Student):
    def __init__(self, name, grade):
        super().__init__(name, grade)

moji_object = Moji("Moji", 100)
print(moji_object)
