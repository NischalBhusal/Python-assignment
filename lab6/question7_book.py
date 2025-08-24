class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# Test the Book class
if __name__ == "__main__":
    book = Book("1984", "Bishnu Prasad")
    print(book)
