class file:
    def __init__(self, filename, type):
        self.filename = filename
        self.type = type
    def __str__(self):
        return f"File: {self.filename}, Type: {self.type}"
    
location = input("What is the location of your file: ")
