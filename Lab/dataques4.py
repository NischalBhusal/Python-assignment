my_string = "hello world"
char_count = {}
for char in my_string:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
