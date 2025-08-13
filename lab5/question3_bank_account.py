# Question 3: BankAccount Class with Banking Operations
# Create a class BankAccount with deposit, withdraw, and balance management

from datetime import datetime

class BankAccount:
    # Class variables
    total_accounts = 0
    bank_name = "Python Bank"
    
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
            'description': f'Account created with initial balance'
        })
        
        print(f" Account created successfully!")
        print(f"   Account Holder: {self.account_holder}")
        print(f"   Account Number: {self.account_number}")
        print(f"   Initial Balance: ${self.balance:.2f}")
    
    def deposit(self, amount):
        """
        Method to deposit money into the account
        Args:
            amount (float): Amount to deposit
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print(" Error: Deposit amount must be positive!")
            return False
        
        old_balance = self.balance
        self.balance += amount
        
        # Log transaction
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'DEPOSIT',
            'amount': amount,
            'balance': self.balance,
            'description': f'Deposit of ${amount:.2f}'
        })
        
        print(f" Deposit Successful!")
        print(f"   Amount Deposited: ${amount:.2f}")
        print(f"   Previous Balance: ${old_balance:.2f}")
        print(f"   New Balance: ${self.balance:.2f}")
        
        return True
    
    def withdraw(self, amount):
        """
        Method to withdraw money from the account
        Args:
            amount (float): Amount to withdraw
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print(" Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(" Error: Insufficient funds!")
            print(f"   Requested Amount: ${amount:.2f}")
            print(f"   Available Balance: ${self.balance:.2f}")
            print(f"   Shortage: ${amount - self.balance:.2f}")
            return False
        
        old_balance = self.balance
        self.balance -= amount
        
        # Log transaction
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'WITHDRAWAL',
            'amount': amount,
            'balance': self.balance,
            'description': f'Withdrawal of ${amount:.2f}'
        })
        
        print(f" Withdrawal Successful!")
        print(f"   Amount Withdrawn: ${amount:.2f}")
        print(f"   Previous Balance: ${old_balance:.2f}")
        print(f"   New Balance: ${self.balance:.2f}")
        
        return True
    
    def show_balance(self):
        """
        Method to display the current balance
        """
        print(f"\n ACCOUNT BALANCE")
        print("-" * 30)
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-" * 30)
    
    def transfer(self, recipient_account, amount):
        """
        Method to transfer money to another account
        Args:
            recipient_account (BankAccount): The recipient's bank account
            amount (float): Amount to transfer
        Returns:
            bool: True if successful, False otherwise
        """
        if amount <= 0:
            print(" Error: Transfer amount must be positive!")
            return False
        
        if amount > self.balance:
            print(" Error: Insufficient funds for transfer!")
            return False
        
        # Withdraw from sender
        old_balance = self.balance
        self.balance -= amount
        
        # Deposit to recipient
        recipient_account.balance += amount
        
        # Log transactions
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'TRANSFER_OUT',
            'amount': amount,
            'balance': self.balance,
            'description': f'Transfer to {recipient_account.account_number}'
        })
        
        recipient_account.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'TRANSFER_IN',
            'amount': amount,
            'balance': recipient_account.balance,
            'description': f'Transfer from {self.account_number}'
        })
        
        print(f" Transfer Successful!")
        print(f"   From: {self.account_holder} ({self.account_number})")
        print(f"   To: {recipient_account.account_holder} ({recipient_account.account_number})")
        print(f"   Amount: ${amount:.2f}")
        print(f"   Your New Balance: ${self.balance:.2f}")
        
        return True
    
    def get_transaction_history(self, limit=5):
        """
        Get recent transaction history
        Args:
            limit (int): Number of recent transactions to show
        """
        print(f"\n TRANSACTION HISTORY (Last {min(limit, len(self.transaction_history))} transactions)")
        print("-" * 70)
        print(f"{'Date/Time':<20} {'Type':<15} {'Amount':<12} {'Balance':<12}")
        print("-" * 70)
        
        recent_transactions = self.transaction_history[-limit:]
        for transaction in recent_transactions:
            timestamp = transaction['timestamp'].strftime("%Y-%m-%d %H:%M")
            trans_type = transaction['type']
            amount = f"${transaction['amount']:.2f}"
            balance = f"${transaction['balance']:.2f}"
            print(f"{timestamp:<20} {trans_type:<15} {amount:<12} {balance:<12}")
        
        print("-" * 70)
    
    def apply_interest(self, interest_rate):
        """
        Apply interest to the account balance
        Args:
            interest_rate (float): Interest rate as percentage (e.g., 2.5 for 2.5%)
        """
        if interest_rate < 0:
            print(" Error: Interest rate cannot be negative!")
            return False
        
        interest_amount = self.balance * (interest_rate / 100)
        old_balance = self.balance
        self.balance += interest_amount
        
        # Log transaction
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'type': 'INTEREST',
            'amount': interest_amount,
            'balance': self.balance,
            'description': f'Interest applied at {interest_rate}%'
        })
        
        print(f" Interest Applied!")
        print(f"   Interest Rate: {interest_rate}%")
        print(f"   Interest Amount: ${interest_amount:.2f}")
        print(f"   Previous Balance: ${old_balance:.2f}")
        print(f"   New Balance: ${self.balance:.2f}")
        
        return True
    
    def __str__(self):
        """
        String representation of the BankAccount object
        """
        return f"BankAccount({self.account_holder}, {self.account_number}, ${self.balance:.2f})"
    
    @classmethod
    def get_bank_info(cls):
        """
        Class method to get bank information
        """
        print(f"\n {cls.bank_name} Information")
        print(f"Total Accounts: {cls.total_accounts}")
    
    @classmethod
    def create_account_interactive(cls):
        """
        Class method to create account interactively
        Returns:
            BankAccount: New bank account object
        """
        try:
            holder = input("Enter account holder name: ").strip()
            account_num = input("Enter account number: ").strip()
            initial = input("Enter initial balance (or press Enter for $0): ").strip()
            
            initial_balance = float(initial) if initial else 0.0
            
            return cls(holder, account_num, initial_balance)
        except ValueError:
            print(" Invalid balance amount. Setting to $0.")
            return cls(holder, account_num, 0.0)

# Demonstration and Testing
if __name__ == "__main__":
    print("=" * 60)
    print("QUESTION 3: BANK ACCOUNT CLASS DEMONSTRATION")
    print("=" * 60)
    
    # 1. Create BankAccount object as required
    print("\n1. Creating BankAccount object:")
    account = BankAccount("John Doe", "ACC001", 1000.0)
    
    # 2. Perform deposit as required
    print("\n2. Performing deposit:")
    account.deposit(500.0)
    
    # 3. Perform withdrawal as required
    print("\n3. Performing withdrawal:")
    account.withdraw(200.0)
    
    # 4. Show balance as required
    print("\n4. Showing current balance:")
    account.show_balance()
    
    # 5. Additional demonstrations
    print("\n5. Additional Banking Operations:")
    
    # Create another account for transfer demo
    print("\nCreating second account:")
    account2 = BankAccount("Jane Smith", "ACC002", 750.0)
    
    # Transfer between accounts
    print("\nPerforming transfer:")
    account.transfer(account2, 300.0)
    
    # Show both balances
    account.show_balance()
    account2.show_balance()
    
    # Apply interest
    print("\nApplying interest:")
    account.apply_interest(2.5)  # 2.5% interest
    account2.apply_interest(2.5)
    
    # 6. Transaction history
    print("\n6. Transaction History:")
    account.get_transaction_history()
    account2.get_transaction_history()
    
    # 7. Error handling demonstrations
    print("\n7. Error Handling Demonstrations:")
    
    print("\nTrying to withdraw more than balance:")
    account.withdraw(5000.0)  # Should fail
    
    print("\nTrying negative deposit:")
    account.deposit(-100.0)  # Should fail
    
    print("\nTrying negative withdrawal:")
    account.withdraw(-50.0)  # Should fail
    
    # 8. Multiple accounts demonstration
    print("\n8. Multiple Accounts Management:")
    accounts = [account, account2]
    
    # Create a third account
    account3 = BankAccount("Bob Johnson", "ACC003", 2000.0)
    accounts.append(account3)
    
    print("\n All Accounts Summary:")
    total_bank_balance = 0
    print(f"{'Account Holder':<15} {'Account #':<10} {'Balance':<12}")
    print("-" * 40)
    
    for acc in accounts:
        print(f"{acc.account_holder:<15} {acc.account_number:<10} ${acc.balance:<11.2f}")
        total_bank_balance += acc.balance
    
    print("-" * 40)
    print(f"{'Total Bank Balance:':<25} ${total_bank_balance:.2f}")
    
    # Bank information
    BankAccount.get_bank_info()
    
    # 9. Interactive account creation
    print("\n9. Interactive Account Creation:")
    try:
        create_new = input("Would you like to create a new account? (y/n): ").lower()
        if create_new == 'y':
            new_account = BankAccount.create_account_interactive()
            new_account.show_balance()
            
            # Perform some operations
            deposit_amount = input("Enter amount to deposit (or press Enter to skip): ").strip()
            if deposit_amount:
                new_account.deposit(float(deposit_amount))
                new_account.show_balance()
                
    except (ValueError, KeyboardInterrupt):
        print("\nAccount creation cancelled or invalid input.")
    
    # 10. Final summary
    print("\n10. Final Account States:")
    for i, acc in enumerate(accounts, 1):
        print(f"Account {i}: {acc}")
    
    print("\n" + "=" * 60)
    print("BANK ACCOUNT CLASS DEMONSTRATION COMPLETED!")
    print("Key Concepts: Constructor, Methods, Object State, Error Handling")
    print("Features: Deposit, Withdraw, Balance, Transfer, Interest, History")
    print("=" * 60)
