import os
import shutil

class FileOrganizer:
    def __init__(self):
        self.location = ""
        self.mp_three_folder = ""
        self.mp_four_folder = ""

    def organize_files(self):
        # Get user input for file locations
        self.location = input("What is the location of your file: ").strip()
        self.mp_three_folder = input("What location do you want your MP3 files to be in: ").strip()
        self.mp_four_folder = input("What location do you want your MP4 files to be in: ").strip()
        
        self.ensure_folders_exist()
        self.move_file()

    def ensure_folders_exist(self):
        # Check if the specified folders exist, if not, create them
        if not os.path.exists(self.mp_three_folder):
            os.makedirs(self.mp_three_folder)
        if not os.path.exists(self.mp_four_folder):
            os.makedirs(self.mp_four_folder)

    def move_file(self):
        # Move the file based on its type
        if self.location.endswith('.mp3'):
            shutil.move(self.location, self.mp_three_folder)
            print(f"Moved MP3 file to {self.mp_three_folder}")
        elif self.location.endswith('.mp4'):
            shutil.move(self.location, self.mp_four_folder)
            print(f"Moved MP4 file to {self.mp_four_folder}")
        else:
            print("Unsupported file type. Only MP3 and MP4 files are handled.")

# Usage
organizer = FileOrganizer()
organizer.organize_files()
