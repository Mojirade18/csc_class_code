# This snippet is to evaluate a user's age and income to provide insights about their statuS and financial stability
print("Hello there!")
age = int(input("How old are you? "))
income = int(input("What is the approximate amount you earn monthly? "))
if age >= 18: print("You are an adult")
if age >= 18 and income > 500000:
    print("You are eligible to work.")
elif age < 18 and income <= 500000:
    print("I think you would mostlikely gets broken soon")
    print("so dont just bother working")
elif age >= 18 and income < 500000:
    print("You are eligible to work but you need to find a better job")
elif age < 18 and income > 500000:
    print("You dey do yahoo?")
else:
    print("wrong input")