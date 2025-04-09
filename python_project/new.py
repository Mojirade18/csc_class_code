class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} 📚 says: 'School is fun!' 🎉"

class Moji(Student):
    def __init__(self, name, grade, favorite_subject):
        super().__init__(name, grade)
        self.favorite_subject = favorite_subject

    def __str__(self):
        return (
            f"{self.name} 🤓 says: 'Learning is awesome!' 💡\n"
            f"Grade: {self.grade} 🏆\n"
            f"Favorite subject: {self.favorite_subject} ❤️"
        )

moji_object = Moji("Moji", 100, "Physics")
print(moji_object)
