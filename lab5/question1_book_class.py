import json

# Question 1: Book Class with Constructor and Methods
# Create a class Book with attributes title, author, and price

class Book:
    def __init__(self, title, author, price):
        """
        Constructor to initialize Book object with title, author, and price
        Args:
            title (str): The title of the book
            author (str): The author of the book
            price (float): The price of the book
        """
        self.title = title
        self.author = author
        self.price = price
        print(f" Book object created: '{self.title}' by {self.author}")
    
    def display_info(self):
        """
        Method to display book's title, author, and price
        """
        print("\n BOOK INFORMATION")
        print("-" * 30)
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: NPR {self.price:.2f}")
        print("-" * 30)
    
    def update_price(self, new_price):
        """
        Method to update the book's price
        Args:
            new_price (float): The new price for the book
        """
        if new_price < 0:
            print(" Error: Price cannot be negative!")
            return False
        
        old_price = self.price
        self.price = new_price
        print(f" Price updated for '{self.title}':")
        print(f"   Old Price: NPR {old_price:.2f}")
        print(f"   New Price: NPR {self.price:.2f}")
        return True
    
    def get_formatted_info(self):
        """
        Method to return formatted book information as string
        Returns:
            str: Formatted book information
        """
        return f"'{self.title}' by {self.author} - NPR {self.price:.2f}"
    
    def apply_discount(self, discount_percent):
        """
        Method to apply discount to the book price
        Args:
            discount_percent (float): Discount percentage (0-100)
        """
        if not (0 <= discount_percent <= 100):
            print(" Error: Discount must be between 0% and 100%!")
            return False
        
        discount_amount = self.price * (discount_percent / 100)
        old_price = self.price
        self.price = old_price - discount_amount
        
        print(f" Discount applied to '{self.title}':")
        print(f"   Original Price: NPR {old_price:.2f}")
        print(f"   Discount: {discount_percent}% (${discount_amount:.2f})")
        print(f"   Final Price: NPR {self.price:.2f}")
        return True
    
    def __str__(self):
        """
        String representation of the Book object
        """
        return f"Book('{self.title}', '{self.author}', NPR {self.price:.2f})"

def save_books_to_file(books, filename="books_data.json"):
    """
    Save book data to a JSON file
    Args:
        books (list): List of Book objects
        filename (str): Name of the file to save data (default: "books_data.json")
    """
    data = [
        {
            "title": book.title,
            "author": book.author,
            "price": book.price
        } for book in books
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_books_from_file(filename="books_data.json"):
    """
    Load book data from a JSON file
    Args:
        filename (str): Name of the file to load data from (default: "books_data.json")
    Returns:
        list: List of Book objects
    """
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:  # Check if the file is not empty
                data = json.loads(content)
                for item in data:
                    books.append(Book(item["title"], item["author"], item["price"]))
    except FileNotFoundError:
        print("No previous book data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Corrupted or empty data found in the file. Starting fresh.")
    return books

# Demonstration and Testing
if __name__ == "__main__":
    print("=" * 30)
    print("BOOK CLASS DEMO")
    print("=" * 30)

    # Load existing books
    books = load_books_from_file()

    while True:
        print("\n1. Add Book | 2. View Books | 3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            price = float(input("Enter book price: "))
            new_book = Book(title, author, price)
            books.append(new_book)
            save_books_to_file(books)
            print("Book added successfully!")

        elif choice == "2":
            if not books:
                print("No books available.")
            else:
                print("\nBooks in the collection:")
                for book in books:
                    print(book.get_formatted_info())

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
