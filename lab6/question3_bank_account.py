class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount")

    def get_account_details(self):
        return f"Account Number: {self.__account_number}, Balance: {self.__balance}"

# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789")
    account.deposit(1000)
    account.withdraw(500)
    print(account.get_account_details())
