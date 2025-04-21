class Task:
    total_tasks = 0

    def __init__(self, time, notes, location):
        self.time = time
        self.notes = notes
        self.location = location
        Task.total_tasks += 1
        self.number = Task.total_tasks  # Automatically assign a unique number

    def __str__(self):
        return f"Task #{self.number}: {self.notes} at {self.location} on {self.time}. Total tasks: {Task.total_tasks}"


class Prep_Tasks(Task):
    def __init__(self, time, notes, location, allow):
        super().__init__(time, notes, location)
        self.allow = allow

    def __str__(self):
        base = super().__str__()
        return f"{base} | Prep Task Allowed: {self.allow}"
