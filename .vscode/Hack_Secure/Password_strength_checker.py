def length(password):
    length_of_pass = 0
    for x in password:
        length_of_pass += 1
    if length_of_pass < range(8, 127):
        print("Please increase the length of your password.\nThank you")
def uppercase():
    pass
def lowercase():
    pass
def number():
    pass
def special_character():
    pass

print ("Hey there this is a password checker")
password = input("Input you password: ")
length(password)