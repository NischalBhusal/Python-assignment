# Set Methods Example

# Original sets
set1 = {1, 2, 3}
set2 = {4, 5}

# Method 1: add
set1.add(6)
print("After add():", set1)

# Method 2: remove
set1.remove(2)
print("After remove():", set1)

# Method 3: union
combined_set = set1.union(set2)
print("After union():", combined_set)
