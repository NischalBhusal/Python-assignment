import random

# Generate a set of 15 unique random digits (as strings)
random_digits_set = set()
while len(random_digits_set) < 15:
    random_digits_set.add(str(random.randint(0, 9)))

# Convert set to a sorted list and then to a string
random_digits_list = sorted(list(random_digits_set))
random_number = ''.join(random_digits_list)

# If you still want to split into 3-digit sets (will be 5 sets of 3 digits each)
number_sets = [random_number[i:i+3] for i in range(0, 15, 3)]

# Calculate the sum of digits for each set
sums = [sum(int(digit) for digit in num_set) for num_set in number_sets]

# Find the set with the highest sum
max_sum = max(sums)
winner_index = sums.index(max_sum)
winner_set = number_sets[winner_index]

print("Your 15 unique random digits (as a set):", random_digits_set)
print("Sorted 15-digit number:", random_number)
print("Number sets:", number_sets)
print("Sums:", sums)
print(f"The winning set is {winner_set} with a sum of {max_sum}!")