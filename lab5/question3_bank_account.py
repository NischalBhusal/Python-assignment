# Question 3: BankAccount Class with Banking Operations
# Create a class BankAccount with deposit, withdraw, and balance management

from datetime import datetime
import json

class BankAccount:
    # Class variables
    total_accounts = 0
    bank_name = "Nepal Bank"
    
    def __init__(self, account_holder, account_number, initial_balance=0.0):
        """
        Constructor to initialize BankAccount object
        Args:
            account_holder (str): Name of the account holder
            account_number (str): Unique account number
            initial_balance (float): Initial balance (default: 0.0)
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
        
        # Increment total accounts
        BankAccount.total_accounts += 1
        
        # Log account creation
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'ACCOUNT_CREATED',
            'amount': initial_balance,
            'balance': self.balance,
            'description': 'Account created with initial balance'
        })
        
    def deposit(self, amount):
        """
        Method to deposit money into the account
        Args:
            amount (float): Amount to deposit
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        
        # Log transaction
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'DEPOSIT',
            'amount': amount,
            'balance': self.balance,
            'description': f'Deposit of NPR {amount:.2f}'
        })
        
        return True
    
    def withdraw(self, amount):
        """
        Method to withdraw money from the account
        Args:
            amount (float): Amount to withdraw
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0 or amount > self.balance:
            print("Error: Invalid withdrawal amount!")
            return False
        
        self.balance -= amount
        
        # Log transaction
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'WITHDRAWAL',
            'amount': amount,
            'balance': self.balance,
            'description': f'Withdrawal of NPR {amount:.2f}'
        })
        
        return True
    
    def show_balance(self):
        """
        Method to display the current balance
        """
        print(f"Account: {self.account_holder} | Balance: NPR {self.balance:.2f}")
    
    def save_to_file(self, filename="bank_accounts.json"):
        """
        Save account data to a JSON file
        Args:
            filename (str): Name of the file to save data (default: "bank_accounts.json")
        """
        try:
            # Load existing data if the file exists
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    existing_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Add the current account data
            data = {
                "account_holder": self.account_holder,
                "account_number": self.account_number,
                "balance": self.balance,
                "transaction_history": [
                    {
                        **transaction,
                        "timestamp": transaction["timestamp"].isoformat()
                    } for transaction in self.transaction_history
                ]
            }
            existing_data.append(data)

            # Save the updated data back to the file
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving account data: {e}")


def load_accounts_from_file(filename="bank_accounts.json"):
    """
    Load account data from a JSON file
    Args:
        filename (str): Name of the file to load data from (default: "bank_accounts.json")
    Returns:
        list: List of BankAccount objects
    """
    accounts = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data_list = json.load(file)
            for data in data_list:
                account = BankAccount(
                    data["account_holder"],
                    data["account_number"],
                    data["balance"]
                )
                account.transaction_history = [
                    {
                        **transaction,
                        "timestamp": datetime.fromisoformat(transaction["timestamp"])
                    } for transaction in data["transaction_history"]
                ]
                accounts.append(account)
    except FileNotFoundError:
        print("No previous account data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Corrupted data found in the file. Resetting the file.")
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error loading account data: {e}")
    return accounts

# Demonstration and Testing
if __name__ == "__main__":
    print("=" * 40)
    print("NEPAL BANK - ACCOUNT MANAGEMENT")
    print("=" * 40)

    # Load existing accounts
    accounts = load_accounts_from_file()

    while True:
        print("\n1. Create Account | 2. Deposit | 3. Withdraw")
        print("4. Show Balance   | 5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            account_number = input("Account No: ")
            initial_balance = float(input("Initial Balance: "))
            account = BankAccount(name, account_number, initial_balance)
            accounts.append(account)
            account.save_to_file()
            print("Account created!")

        elif choice == "2":
            account_number = input("Account No: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                amount = float(input("Deposit Amount: "))
                if account.deposit(amount):
                    account.save_to_file()
                    print("Deposit successful!")
            else:
                print("Account not found!")

        elif choice == "3":
            account_number = input("Account No: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                amount = float(input("Withdraw Amount: "))
                if account.withdraw(amount):
                    account.save_to_file()
                    print("Withdrawal successful!")
            else:
                print("Account not found!")

        elif choice == "4":
            account_number = input("Account No: ")
            account = next((acc for acc in accounts if acc.account_number == account_number), None)
            if account:
                account.show_balance()
            else:
                print("Account not found!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")
