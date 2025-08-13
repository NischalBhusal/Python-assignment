# Question 9: Extract numbers divisible by 10 using filter() and lambda

# Given list of numbers
numbers = [10, 15, 20, 25, 30]

# Use filter() and lambda to extract numbers divisible by 10
divisible_by_10 = list(filter(lambda x: x % 10 == 0, numbers))

# Display results
print("Original list:", numbers)
print("Numbers divisible by 10:", divisible_by_10)
