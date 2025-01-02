# This snippet is used to print the are of a rectangle

# This gets the vital information needed for running the program
loop = True
while loop:
    try:
        length_of_rectangle = float(input("What is the length of the rectangle? "))
        breadth_of_rectangle = float(input("What is the breadth of the rectangle? "))

# This is where the data is being manipulated
        if length_of_rectangle <= 0 or breadth_of_rectangle <= 0:
            print("Input nataural numbers only.")
            continue
        else:
            area = length_of_rectangle * breadth_of_rectangle
            print(f"The area of your rectangle is {area}")
            loop = False
    except ValueError:
        print("Input only figures")