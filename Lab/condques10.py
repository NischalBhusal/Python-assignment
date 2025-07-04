print("Select Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter choice (1/2/3/4): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b)
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice.")
