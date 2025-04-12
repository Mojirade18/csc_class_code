def length(password):
    length_of_pass = 0
    for x in password:
        length_of_pass += 1
    if length_of_pass < 8:
        print("Please increase the length of your password.\nThank you")
    else:
        print("Your password has a good length\nWeldon")
def uppercase():
    pass
def lowercase():
    pass

def number():
    pass
def special_character():
    pass

print ("Hey there this is a password checker")
password = input("Input you password: ").strip()
length(password)