from datetime import datetime, timedelta
import math

class Student:
    def __init__(self, name, date_of_birth):
        self.__name = name  
        self.__date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.__attendance_dates = [] 
    def get_name(self):
        return self.__name

    
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.__date_of_birth.year
        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age -= 1
        return age

    
    def mark_attendance(self):
        today = datetime.today().date()
        if today not in self.__attendance_dates:
            self.__attendance_dates.append(today)
            print(f"{self.__name} marked present on {today}.")
        else:
            print(f"{self.__name} is already marked present for today.")

    
    def attendance_percentage(self, total_school_days):
        attended_days = len(self.__attendance_dates)
        percentage = (attended_days / total_school_days) * 100
        return round(percentage, 2)

    
    def get_attendance_summary(self):
        return f"{self.__name} has attended {len(self.__attendance_dates)} day(s): {self.__attendance_dates}"


student1 = Student("Amina Yusuf", "2005\S06\15")
print("Name:", student1.get_name())
print("Age:", student1.calculate_age())

# Mark attendance for 3 days (simulated)
student1.mark_attendance()
student1._Student__attendance_dates.append(datetime.today().date() - timedelta(days=1))
student1._Student__attendance_dates.append(datetime.today().date() - timedelta(days=2))

print(student1.get_attendance_summary())
print("Attendance Percentage (out of 20 school days):", student1.attendance_percentage(20), "%")
