# Lab 5: Convert input to int/float list
user_input = input("Enter numbers separated by commas: ")
number_list = []
for num in user_input.split(','):
    num = num.strip()
    if '.' in num:
        number_list.append(float(num))
    else:
        number_list.append(int(num))
print("Converted list:", number_list)



