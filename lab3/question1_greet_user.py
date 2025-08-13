# Question 1: Write a Python function named greet_user that takes a user's name and prints:
# "Hello, <name>! Welcome to Python." Call the function with a sample name.

def greet_user(name):
    """Function that takes a user's name and prints a greeting"""
    print(f"Hello, {name}! Welcome to Python.")

# Demonstration
if __name__ == "__main__":
    print("Question 1: Greet User Function")
    print("-" * 30)
    
    # Call the function with sample names
    greet_user("Alice")
    greet_user("Bob")
    greet_user("Charlie")
    greet_user("Diana")
    
    # Interactive example
    print("\nInteractive Example:")
    user_name = input("Enter your name: ")
    greet_user(user_name)
