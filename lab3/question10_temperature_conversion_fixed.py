# Question 10: Convert Celsius to Fahrenheit and filter above 100°F

# Given list of temperatures in Celsius
temperatures_celsius = [36.5, 37.0, 39.2, 35.6, 38.7]

# Step 1: Convert to Fahrenheit using map()
# Formula: F = (C * 9/5) + 32
temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))

# Step 2: Filter out temperatures above 100°F using filter()
temperatures_above_100f = list(filter(lambda f: f > 100, temperatures_fahrenheit))

# Display results
print("Original Celsius temperatures:", temperatures_celsius)
print("Converted Fahrenheit temperatures:", temperatures_fahrenheit)
print("Temperatures above 100°F:", temperatures_above_100f)
