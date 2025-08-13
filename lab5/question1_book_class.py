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
        print(f"Price: ${self.price:.2f}")
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
        print(f"   Old Price: ${old_price:.2f}")
        print(f"   New Price: ${self.price:.2f}")
        return True
    
    def get_formatted_info(self):
        """
        Method to return formatted book information as string
        Returns:
            str: Formatted book information
        """
        return f"'{self.title}' by {self.author} - ${self.price:.2f}"
    
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
        print(f"   Original Price: ${old_price:.2f}")
        print(f"   Discount: {discount_percent}% (${discount_amount:.2f})")
        print(f"   Final Price: ${self.price:.2f}")
        return True
    
    def __str__(self):
        """
        String representation of the Book object
        """
        return f"Book('{self.title}', '{self.author}', ${self.price:.2f})"

# Demonstration and Testing
if __name__ == "__main__":
    print("=" * 50)
    print("QUESTION 1: BOOK CLASS DEMONSTRATION")
    print("=" * 50)
    
    # 1. Create Book object with sample data
    print("\n1. Creating Book objects with sample data:")
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.50)
    book3 = Book("1984", "George Orwell", 13.25)
    
    # 2. Display book information using display_info() method
    print("\n2. Displaying book information:")
    book1.display_info()
    book2.display_info()
    book3.display_info()
    
    # 3. Update price using update_price() method
    print("\n3. Updating book prices:")
    book1.update_price(15.99)
    book2.update_price(16.75)
    
    # Display updated information
    print("\n4. Displaying updated information:")
    book1.display_info()
    book2.display_info()
    
    # 4. Additional demonstrations
    print("\n5. Additional features:")
    
    # Apply discount
    book3.apply_discount(20)  # 20% discount
    book3.display_info()
    
    # String representation
    print("\n6. String representations:")
    print(f"Book 1: {book1}")
    print(f"Book 2: {book2}")
    print(f"Book 3: {book3}")
    
    # Formatted info
    print("\n7. Formatted information:")
    print(f" {book1.get_formatted_info()}")
    print(f" {book2.get_formatted_info()}")
    print(f" {book3.get_formatted_info()}")
    
    # 5. Interactive example
    print("\n8. Interactive Book Creation:")
    try:
        print("Create your own book:")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        price = float(input("Enter book price: $"))
        
        if title and author and price >= 0:
            user_book = Book(title, author, price)
            user_book.display_info()
            
            # Ask for price update
            update_choice = input("\nWould you like to update the price? (y/n): ").lower()
            if update_choice == 'y':
                new_price = float(input("Enter new price: $"))
                user_book.update_price(new_price)
                user_book.display_info()
                
            # Ask for discount
            discount_choice = input("\nWould you like to apply a discount? (y/n): ").lower()
            if discount_choice == 'y':
                discount = float(input("Enter discount percentage (0-100): "))
                user_book.apply_discount(discount)
                user_book.display_info()
        else:
            print(" Invalid input. Please provide valid title, author, and non-negative price.")
            
    except ValueError:
        print(" Invalid input. Please enter numeric values for price.")
    except EOFError:
        print(" No input available. Creating demonstration book instead...")
        # Create a demonstration book when no input is available
        demo_book = Book("The Catcher in the Rye", "J.D. Salinger", 11.99)
        demo_book.display_info()
        print("Demonstrating price update:")
        demo_book.update_price(13.50)
        demo_book.display_info()
    except KeyboardInterrupt:
        print("\n\n Book creation cancelled.")
    
    # 6. Comparison and collection
    print("\n9. Book Collection Management:")
    book_collection = [book1, book2, book3]
    
    print(" Your Book Collection:")
    total_value = 0
    for i, book in enumerate(book_collection, 1):
        print(f"{i}. {book.get_formatted_info()}")
        total_value += book.price
    
    print(f"\n Total Collection Value: ${total_value:.2f}")
    print(f" Average Book Price: ${total_value / len(book_collection):.2f}")
    
    # Find most expensive book
    most_expensive = max(book_collection, key=lambda b: b.price)
    print(f" Most Expensive: {most_expensive.get_formatted_info()}")
    
    # Find cheapest book
    cheapest = min(book_collection, key=lambda b: b.price)
    print(f" Cheapest: {cheapest.get_formatted_info()}")
    
    print("\n" + "=" * 50)
    print("BOOK CLASS DEMONSTRATION COMPLETED!")
    print("Key Concepts: Constructor, Methods, Object Creation, Self Parameter")
    print("=" * 50)
