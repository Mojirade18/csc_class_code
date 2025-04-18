class Task:
    def __init__(self, name, time, notes, location):
        self.name = name
        self.time = time
        self.notes = notes
        self.location = location
        self.number = 0
        self.number += 1

    def __str__(self):
        total = self.number
        return f"The total amount of task is {self.number}"