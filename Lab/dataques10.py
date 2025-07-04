my_dict = {}
n = int(input("How many key-value pairs you want to enter? "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

search_key = input("Enter key to search: ")
if search_key in my_dict:
    print("Value:", my_dict[search_key])
else:
    print("Key not found.")
