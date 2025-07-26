a = input("Enter your sentence")
a = a.lower()
vowel = []
s = set()
for char in a : 
    if char not in vowel : 
        vowel.append(char)
for element in vowel : 
    if element == "a" or element == "e" or element == "i" or element == "o" or element == "u" : 
        s.add(element)
print(s)