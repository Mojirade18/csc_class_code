import string

def check_length(password):
    if len(password) >= 8:
        print(" Good password length.")
        return 1
    else:
        print(" Password should be at least 8 characters long.")
        return 0

def check_uppercase(password):
    for char in password:
        if char.isupper():
            print(" Contains an uppercase letter.")
            return 1
    print(" Add at least one uppercase letter.")
    return 0

def check_lowercase(password):
    for char in password:
        if char.islower():
            print(" Contains a lowercase letter.")
            return 1
    print(" Add at least one lowercase letter.")
    return 0

def check_number(password):
    for char in password:
        if char.isdigit():
            print(" Contains a number.")
            return 1
    print(" Add at least one number.")
    return 0

def check_special_character(password):
    for char in password:
        if char in string.punctuation:
            print(" Contains a special character.")
            return 1
    print(" Add at least one special character (e.g., !, @, #, etc.).")
    return 0

def determine_strength(score):
    print("\nPassword Strength Rating:")
    if score <= 2:
        print(" Strength: Weak")
    elif score == 3 or score == 4:
        print(" Strength: Moderate")
    elif score == 5:
        print(" Strength: Strong")

def main():
    print("=" * 50)
    print(" Password Strength Checker")
    print("=" * 50)

    while True:
        password = input("\nEnter your password: ").strip()
        print("\nEvaluating your password...\n")

        score = 0
        score += check_length(password)
        score += check_uppercase(password)
        score += check_lowercase(password)
        score += check_number(password)
        score += check_special_character(password)

        determine_strength(score)

        retry = input("\nWould you like to test another password? (yes/no): ").strip().lower()
        if retry != "yes":
            print("\nThank you for using the Password Strength Checker. Stay secure!")
            break

if __name__ == "__main__":
    main()
