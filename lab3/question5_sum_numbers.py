# Question 5: Create a function to sum numbers using *args

def sum_numbers(*args):
    """
    Function to calculate the sum of any number of numeric arguments.
    """
    return sum(args)

# Test the function with 2, 3, and 5 numbers
print("Sum of 2 numbers (10, 20):", sum_numbers(10, 20))
print("Sum of 3 numbers (5, 15, 25):", sum_numbers(5, 15, 25))
print("Sum of 5 numbers (1, 2, 3, 4, 5):", sum_numbers(1, 2, 3, 4, 5))
