class Task:
    total_tasks = 0  # Class variable to track total number of tasks

    def __init__(self, time, notes, location):
        self.time = time
        self.notes = notes
        self.location = location
        Task.total_tasks += 1
        self.number = Task.total_tasks  # Automatically assign a unique number to each task

    def __str__(self):
        return f"Task #{self.number}: {self.notes} at {self.location} on {self.time}. Total tasks: {Task.total_tasks}"


class Prep_Tasks(Task):
    def __init__(self, time, notes, location, allow):
        super().__init__(time, notes, location)
        self.allow = allow

    def __str__(self):
        base = super().__str__()
        return f"{base} | Prep Task Allowed: {self.allow}"


# --- Example Usage ---
if __name__ == "__main__":
    task1 = Task("10:00 AM", "Team Meeting", "Conference Room")
    task2 = Prep_Tasks("12:00 PM", "Prepare Slides", "Office", allow=True)
    task3 = Task("3:00 PM", "Call Supplier", "Home Office")
    task4 = Prep_Tasks("5:00 PM", "Review Report", "Remote", allow=False)

    print(task1)
    print(task2)
    print(task3)
    print(task4)
