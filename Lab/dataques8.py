names = ["Alice", "Bob", "Alice", "Tom", "Bob", "Tom", "Tom"]
name_count = {}
for name in names:
    name_count[name] = name_count.get(name, 0) + 1
print(name_count)
