# Lab 4: File Handling Projects

This folder contains two comprehensive CLI applications demonstrating file handling, exception management, and practical programming concepts.

## Project 1: CLI Contact Book (`project1_contact_book.py`)

### Features:
 **Add new contact** - Append to file with duplicate checking  
 **View all contacts** - Read and display formatted contact list  
 **Search contacts** - Filter by name or phone number  
 **Update contact** - Modify existing contact information  
 **Delete contact** - Remove contacts from file  
 **Export contacts** - Create backup files  
 **Exception handling** - File not found, permission errors, etc.

### File Used:
- `contacts.txt` - Stores contact information in format: Name,Phone

### How to Run:
```bash
python project1_contact_book.py
```

### Sample Usage:
1. Add contacts: John Doe, 555-1234
2. Search for "John" or "555"
3. View all contacts in formatted table
4. Update phone numbers
5. Export backup files

### Error Handling:
- File not found errors
- Permission denied errors
- Invalid input validation
- Duplicate contact checking
- Empty field validation

---

## Project 2: Simple Banking System (`project2_banking_system.py`)

### Features:
 **Create account** - New customer registration  
 **Deposit money** - Add funds with transaction logging  
 **Withdraw money** - Remove funds with balance checking  
 **View account details** - Display customer information  
 **Transaction history** - Show recent transactions  
 **View all customers** - Admin view of all accounts  
 **Exception handling** - File errors, insufficient funds, etc.

### Files Used:
- `customers.txt` - Stores customer records: Name,AccountNumber,Balance
- `transactions.txt` - Logs all transactions with timestamps

### How to Run:
```bash
python project2_banking_system.py
```

### Sample Usage:
1. Create account: "John Doe", Account "ACC001", $1000 initial balance
2. Deposit $500 to ACC001
3. Withdraw $200 from ACC001
4. View transaction history
5. Check all customer accounts

### Error Handling:
- Account not found errors
- Insufficient funds checking
- Negative amount validation
- File permission errors
- Data corruption recovery

---

## Technical Features Demonstrated:

### File Operations:
- **Reading files** - `open(file, 'r')`
- **Writing files** - `open(file, 'w')`
- **Appending files** - `open(file, 'a')`
- **File existence checking** - `os.path.exists()`

### Exception Handling:
- `FileNotFoundError` - Handle missing files
- `PermissionError` - Handle access issues
- `ValueError` - Handle invalid data
- `KeyboardInterrupt` - Graceful exit on Ctrl+C

### Data Processing:
- **CSV-style parsing** - Split by commas
- **Data validation** - Check required fields
- **Search and filter** - Find specific records
- **Update operations** - Modify existing data

### User Interface:
- **Menu-driven interface** - Clear navigation
- **Input validation** - Error checking
- **Formatted output** - Table displays
- **User feedback** - Success/error messages

---

## File Formats:

### contacts.txt:
```
# Contact Book - Format: Name,Phone
John Doe,555-1234
Jane Smith,555-5678
```

### customers.txt:
```
# Banking System - Format: Name,AccountNumber,Balance
John Doe,ACC001,1000.00
Jane Smith,ACC002,1500.50
```

### transactions.txt:
```
# Transaction Log - Format: Timestamp,AccountNumber,Type,Amount,NewBalance
2025-08-13 10:30:15,ACC001,DEPOSIT,500.00,1500.00
2025-08-13 11:15:22,ACC001,WITHDRAWAL,200.00,1300.00
```

---

## Running the Projects:

### Prerequisites:
- Python 3.6 or higher
- Write permissions in the project directory

### Quick Start:

**Contact Book:**
```bash
cd "Python assignment/lab4"
python project1_contact_book.py
```

**Banking System:**
```bash
cd "Python assignment/lab4"
python project2_banking_system.py
```

### Testing:
Both projects include comprehensive error handling and will create necessary files automatically on first run.

---

## Learning Objectives Achieved:

1. **File I/O Operations** - Reading, writing, appending files
2. **Exception Handling** - Graceful error management
3. **Data Persistence** - Storing and retrieving data
4. **User Interface Design** - Menu-driven applications
5. **Data Validation** - Input checking and sanitization
6. **Search and Filter** - Data querying operations
7. **Transaction Logging** - Audit trail implementation
8. **Backup Operations** - Data export functionality

Both projects demonstrate practical, real-world applications of file handling in Python with robust error handling and user-friendly interfaces.
