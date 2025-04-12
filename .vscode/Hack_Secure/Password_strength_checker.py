def length(password):
    length_of_pass = 0
    for x in password:
        length_of_pass += 1
    if length_of_pass < 8:
        print("Please increase the length of your password.\nThank you")
    else:
        print("Your password has a good length\nWeldon")
def uppercase(password):
    for x in password:
        if x.isupper():
            print("Your password has an uppercase\nThats a very good way of creating a password.")
        else:
            print("Please input an uppercase in yor password.")
def lowercase():
    pass

def number():
    pass
def special_character():
    pass

print ("Hey there this is a password checker")
while True:
    password = input("Input you password: ").strip()
    length(password)