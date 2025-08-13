# Question 4: Create a function to print book details using keyword arguments

def book_info(title, author, year):
    """
    Function to print book details.
    Args:
        title (str): Title of the book
        author (str): Author of the book
        year (int): Year of publication
    """
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

# Call the function using keyword arguments in different orders
print("Call 1:")
book_info(title="1984", author="George Orwell", year=1949)

print("\nCall 2:")
book_info(author="J.K. Rowling", year=1997, title="Harry Potter and the Philosopher's Stone")

print("\nCall 3:")
book_info(year=1813, title="Pride and Prejudice", author="Jane Austen")
