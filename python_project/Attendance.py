from datetime import datetime, timedelta

class Student:
    def __init__(self, name, date_of_birth):
        self.name = name
        #date_of_birth is converted from string to a datetime object using strptime.
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.attendance_dates = set()

    def get_name(self):
        return self.__name

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.__date_of_birth.year
        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age -= 1
        return age

    def mark_attendance(self, date=None):
        if date is None:
            date = datetime.today().date()
        else:
            date = datetime.strptime(date, "%Y-%m-%d").date()

        if date not in self.__attendance_dates:
            self.__attendance_dates.add(date)
            print(f"{self.__name} marked present on {date}.")
        else:
            print(f"{self.__name} is already marked present for {date}.")

    def attendance_percentage(self, total_school_days):
        if total_school_days <= 0:
            return 0.0
        attended_days = len(self.__attendance_dates)
        percentage = (attended_days / total_school_days) * 100
        return round(percentage, 2)

    def get_attendance_summary(self):
        sorted_dates = sorted(self.__attendance_dates)
        summary = f"{self.__name} has attended {len(sorted_dates)} day(s):\n"
        for date in sorted_dates:
            summary += f" - {date}\n"
        return summary


# Demo
name = input("Enter the name of the student: ")
date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ")
student1 = Student(name, date_of_birth)
print("Name of student:", student1.get_name())
print("Age of student:", student1.calculate_age())

# Mark attendance for today and 2 previous days
student1.mark_attendance()
student1.mark_attendance((datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d"))
student1.mark_attendance((datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d"))

print(student1.get_attendance_summary())
print("Attendance Percentages (out of 20 school days):", student1.attendance_percentage(20), "%")
