# Project 2: Simple Banking System
# A file-based banking system with deposits, withdrawals, and transaction logging

import os
from datetime import datetime
import csv

class BankingSystem:
    def __init__(self, customers_file="customers.txt", transactions_file="transactions.txt"):
        self.customers_file = customers_file
        self.transactions_file = transactions_file
        self.ensure_files_exist()
    
    def ensure_files_exist(self):
        """Create necessary files if they don't exist"""
        try:
            # Create customers file
            if not os.path.exists(self.customers_file):
                with open(self.customers_file, 'w') as file:
                    file.write("# Banking System - Format: Name,AccountNumber,Balance\n")
                print(f"Created customer database: {self.customers_file}")
            
            # Create transactions file
            if not os.path.exists(self.transactions_file):
                with open(self.transactions_file, 'w') as file:
                    file.write("# Transaction Log - Format: Timestamp,AccountNumber,Type,Amount,NewBalance\n")
                print(f"Created transaction log: {self.transactions_file}")
                
        except Exception as e:
            print(f"Error creating files: {e}")
    
    def create_account(self, name, account_number, initial_balance=0.0):
        """Create a new customer account"""
        try:
            # Validate input
            if not name.strip() or not account_number.strip():
                print("Error: Name and account number cannot be empty!")
                return False
            
            if initial_balance < 0:
                print("Error: Initial balance cannot be negative!")
                return False
            
            # Check if account already exists
            if self.account_exists(account_number):
                print(f"Error: Account {account_number} already exists!")
                return False
            
            # Add new customer
            with open(self.customers_file, 'a') as file:
                file.write(f"{name},{account_number},{initial_balance:.2f}\n")
            
            # Log account creation
            self.log_transaction(account_number, "ACCOUNT_CREATED", initial_balance, initial_balance)
            
            print(f" Account created successfully!")
            print(f"   Name: {name}")
            print(f"   Account Number: {account_number}")
            print(f"   Initial Balance: ${initial_balance:.2f}")
            
            return True
            
        except Exception as e:
            print(f"Error creating account: {e}")
            return False
    
    def account_exists(self, account_number):
        """Check if an account exists"""
        try:
            with open(self.customers_file, 'r') as file:
                lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        _, acc_num, _ = line.split(',')
                        if acc_num == account_number:
                            return True
                    except ValueError:
                        continue
            return False
            
        except FileNotFoundError:
            return False
        except Exception:
            return False
    
    def get_customer_info(self, account_number):
        """Get customer information by account number"""
        try:
            with open(self.customers_file, 'r') as file:
                lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        name, acc_num, balance = line.split(',')
                        if acc_num == account_number:
                            return {
                                'name': name,
                                'account_number': acc_num,
                                'balance': float(balance)
                            }
                    except ValueError:
                        continue
            return None
            
        except FileNotFoundError:
            print(f"Error: Customer file '{self.customers_file}' not found!")
            return None
        except Exception as e:
            print(f"Error reading customer info: {e}")
            return None
    
    def update_balance(self, account_number, new_balance):
        """Update customer balance in the file"""
        try:
            with open(self.customers_file, 'r') as file:
                lines = file.readlines()
            
            updated = False
            updated_lines = []
            
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    try:
                        name, acc_num, old_balance = line.strip().split(',')
                        if acc_num == account_number:
                            updated_lines.append(f"{name},{acc_num},{new_balance:.2f}\n")
                            updated = True
                        else:
                            updated_lines.append(line)
                    except ValueError:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
            
            if updated:
                with open(self.customers_file, 'w') as file:
                    file.writelines(updated_lines)
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Error updating balance: {e}")
            return False
    
    def deposit(self, account_number, amount):
        """Deposit money to an account"""
        try:
            # Validate amount
            if amount <= 0:
                print("Error: Deposit amount must be positive!")
                return False
            
            # Get current customer info
            customer = self.get_customer_info(account_number)
            if not customer:
                print(f"Error: Account {account_number} not found!")
                return False
            
            # Calculate new balance
            old_balance = customer['balance']
            new_balance = old_balance + amount
            
            # Update balance
            if self.update_balance(account_number, new_balance):
                # Log transaction
                self.log_transaction(account_number, "DEPOSIT", amount, new_balance)
                
                print(f" Deposit successful!")
                print(f"   Account: {account_number} ({customer['name']})")
                print(f"   Deposited: ${amount:.2f}")
                print(f"   Previous Balance: ${old_balance:.2f}")
                print(f"   New Balance: ${new_balance:.2f}")
                
                return True
            else:
                print("Error: Failed to update balance!")
                return False
                
        except Exception as e:
            print(f"Error processing deposit: {e}")
            return False
    
    def withdraw(self, account_number, amount):
        """Withdraw money from an account"""
        try:
            # Validate amount
            if amount <= 0:
                print("Error: Withdrawal amount must be positive!")
                return False
            
            # Get current customer info
            customer = self.get_customer_info(account_number)
            if not customer:
                print(f"Error: Account {account_number} not found!")
                return False
            
            # Check sufficient funds
            old_balance = customer['balance']
            if amount > old_balance:
                print(f"Error: Insufficient funds!")
                print(f"   Requested: ${amount:.2f}")
                print(f"   Available: ${old_balance:.2f}")
                return False
            
            # Calculate new balance
            new_balance = old_balance - amount
            
            # Update balance
            if self.update_balance(account_number, new_balance):
                # Log transaction
                self.log_transaction(account_number, "WITHDRAWAL", amount, new_balance)
                
                print(f" Withdrawal successful!")
                print(f"   Account: {account_number} ({customer['name']})")
                print(f"   Withdrawn: ${amount:.2f}")
                print(f"   Previous Balance: ${old_balance:.2f}")
                print(f"   New Balance: ${new_balance:.2f}")
                
                return True
            else:
                print("Error: Failed to update balance!")
                return False
                
        except Exception as e:
            print(f"Error processing withdrawal: {e}")
            return False
    
    def log_transaction(self, account_number, transaction_type, amount, new_balance):
        """Log transaction to the transactions file"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.transactions_file, 'a') as file:
                file.write(f"{timestamp},{account_number},{transaction_type},{amount:.2f},{new_balance:.2f}\n")
                
        except Exception as e:
            print(f"Warning: Failed to log transaction: {e}")
    
    def view_account_details(self, account_number):
        """View detailed account information"""
        try:
            customer = self.get_customer_info(account_number)
            if not customer:
                print(f"Account {account_number} not found!")
                return
            
            print(f"\n ACCOUNT DETAILS")
            print("="*40)
            print(f"Name: {customer['name']}")
            print(f"Account Number: {customer['account_number']}")
            print(f"Current Balance: ${customer['balance']:.2f}")
            print("="*40)
            
            # Show recent transactions
            self.view_transaction_history(account_number, limit=5)
            
        except Exception as e:
            print(f"Error viewing account details: {e}")
    
    def view_transaction_history(self, account_number, limit=10):
        """View transaction history for an account"""
        try:
            transactions = []
            
            with open(self.transactions_file, 'r') as file:
                lines = file.readlines()
            
            # Collect transactions for this account
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        timestamp, acc_num, trans_type, amount, balance = line.split(',')
                        if acc_num == account_number:
                            transactions.append({
                                'timestamp': timestamp,
                                'type': trans_type,
                                'amount': float(amount),
                                'balance': float(balance)
                            })
                    except ValueError:
                        continue
            
            if not transactions:
                print(f" No transaction history found for account {account_number}")
                return
            
            print(f"\n TRANSACTION HISTORY (Last {min(limit, len(transactions))} transactions)")
            print("="*80)
            print(f"{'Date/Time':<20} {'Type':<15} {'Amount':<12} {'Balance':<12}")
            print("-"*80)
            
            # Show most recent transactions first
            for transaction in transactions[-limit:]:
                amount_str = f"${transaction['amount']:.2f}"
                balance_str = f"${transaction['balance']:.2f}"
                print(f"{transaction['timestamp']:<20} {transaction['type']:<15} {amount_str:<12} {balance_str:<12}")
            
            print("-"*80)
            print(f"Total transactions: {len(transactions)}")
            
        except FileNotFoundError:
            print(f"No transaction history file found.")
        except Exception as e:
            print(f"Error viewing transaction history: {e}")
    
    def view_all_customers(self):
        """View all customer accounts"""
        try:
            with open(self.customers_file, 'r') as file:
                lines = file.readlines()
            
            customers = []
            total_balance = 0
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        name, acc_num, balance = line.split(',')
                        customers.append({
                            'name': name,
                            'account': acc_num,
                            'balance': float(balance)
                        })
                        total_balance += float(balance)
                    except ValueError:
                        continue
            
            if not customers:
                print(" No customers found in the system.")
                return
            
            print(f"\n ALL CUSTOMERS")
            print("="*60)
            print(f"{'Name':<20} {'Account Number':<15} {'Balance':<12}")
            print("-"*60)
            
            for customer in customers:
                balance_str = f"${customer['balance']:.2f}"
                print(f"{customer['name']:<20} {customer['account']:<15} {balance_str:<12}")
            
            print("-"*60)
            print(f"Total Customers: {len(customers)}")
            print(f"Total Bank Balance: ${total_balance:.2f}")
            
        except FileNotFoundError:
            print(f"Error: Customer file '{self.customers_file}' not found!")
        except Exception as e:
            print(f"Error viewing customers: {e}")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print(" SIMPLE BANKING SYSTEM")
    print("="*50)
    print("1. Create new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View account details")
    print("5. View transaction history")
    print("6. View all customers")
    print("7. Exit")
    print("-"*50)

def main():
    """Main function to run the banking system"""
    bank = BankingSystem()
    
    print(" Welcome to Simple Banking System!")
    print("Customer data: customers.txt | Transaction log: transactions.txt")
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                print("\n CREATE NEW ACCOUNT")
                name = input("Enter customer name: ").strip()
                account_number = input("Enter account number: ").strip()
                initial_balance = input("Enter initial balance (0 if none): ").strip()
                
                try:
                    initial_balance = float(initial_balance) if initial_balance else 0.0
                    bank.create_account(name, account_number, initial_balance)
                except ValueError:
                    print("Invalid balance amount!")
                    
            elif choice == '2':
                print("\n DEPOSIT MONEY")
                account_number = input("Enter account number: ").strip()
                amount = input("Enter deposit amount: ").strip()
                
                try:
                    amount = float(amount)
                    bank.deposit(account_number, amount)
                except ValueError:
                    print("Invalid amount!")
                    
            elif choice == '3':
                print("\n WITHDRAW MONEY")
                account_number = input("Enter account number: ").strip()
                amount = input("Enter withdrawal amount: ").strip()
                
                try:
                    amount = float(amount)
                    bank.withdraw(account_number, amount)
                except ValueError:
                    print("Invalid amount!")
                    
            elif choice == '4':
                print("\n VIEW ACCOUNT DETAILS")
                account_number = input("Enter account number: ").strip()
                bank.view_account_details(account_number)
                
            elif choice == '5':
                print("\n VIEW TRANSACTION HISTORY")
                account_number = input("Enter account number: ").strip()
                limit = input("Enter number of transactions to show (default 10): ").strip()
                
                try:
                    limit = int(limit) if limit else 10
                    bank.view_transaction_history(account_number, limit)
                except ValueError:
                    bank.view_transaction_history(account_number)
                    
            elif choice == '6':
                bank.view_all_customers()
                
            elif choice == '7':
                print("\n Thank you for using Simple Banking System!")
                print("All data is safely stored in files.")
                break
                
            else:
                print(" Invalid choice! Please enter 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n Goodbye! Exiting Banking System...")
            break
        except Exception as e:
            print(f" An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
