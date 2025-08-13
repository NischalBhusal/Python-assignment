# Question 6: Create a function to print student profile using **kwargs

def student_profile(**kwargs):
    """
    Function to print student profile details.
    Accepts key-value pairs as arguments.
    """
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Call the function with at least three named arguments
student_profile(name="John Doe", age=16, grade="10th")
