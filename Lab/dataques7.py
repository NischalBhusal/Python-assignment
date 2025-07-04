dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged = dict1.copy()
for key, value in dict2.items():
    merged[key] = merged.get(key, 0) + value

print("Merged Dictionary:", merged)
