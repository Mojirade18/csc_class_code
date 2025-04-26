
class File:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type

    def __str__(self):
        return f"File: {self.filename}, Type: {self.file_type}"


def organize_files():
    # Get user input for file locations
    location = input("What is the location of your file: ").strip()
    mp_three_file = input("What location do you want your MP3 files to be in: ").strip()
    mp_four_file = input("What location do you want your MP4 files to be in: ").strip()
