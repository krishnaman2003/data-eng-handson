class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.__balance}")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            print("Withdrawal amount must be positive")
    
    def check_balance(self):
        print(f"Current balance: ${self.__balance}")
        return self.__balance


# Example
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()