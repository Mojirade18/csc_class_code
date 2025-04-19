class Task:
    total_tasks = 0
    def __init__(self, time, notes, location):
        self.time = time
        self.notes = notes
        self.location = location
        self.number = 0
        Task.total_tasks += 1

    def __str__(self):
        total = self.number
        return f"The total amount of task is {Task.total_tasks}"

class Prep_Tasks(Task):
    super().__init__()
