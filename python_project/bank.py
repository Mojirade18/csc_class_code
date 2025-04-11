class loan:
    def __init__(self, name, account_number, amount):
        self.account_number = account_number
        self.name = name
        self.amount = amount

    def accept(self, AIB):
        if AIB > 20000:
            return("✅You are eligible to loan money")
        else:
            return("❌You have to have above 20 000 naira in your account")

    def __str__(self):
        return f"Hey {self.name}, welcome to loany bank app."


while True:
    name = input("What is your name? ") 
    account_number = input("What is your account number? ")
    AIB = float(input("How much do you have in your bank account? "))
    user_loan = loan (name, account_number, AIB)
    print(user_loan)