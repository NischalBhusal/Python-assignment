# Question 3: Create a function to calculate power with a default exponent

def power(base, exponent=2):
    """
    Function to calculate the power of a base raised to an exponent.
    Args:
        base (float): The base number
        exponent (int, optional): The exponent. Defaults to 2.
    Returns:
        float: The result of base raised to the power of exponent
    """
    return base ** exponent

# Demonstrate the function with and without the exponent argument
print("With default exponent (2):")
print("5^2 =", power(5))
print("3^2 =", power(3))

print("\nWith custom exponent:")
print("2^3 =", power(2, 3))
print("4^4 =", power(4, 4))
