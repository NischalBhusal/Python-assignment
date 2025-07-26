#Sort the list in ascending order
list1 = []
n = int(input("Enter the number of elements in the list"))
for i in range(n) : 
    a = int(input("Enter your number"))
    list1.append(a)
#Using built-in functions
print(sorted(list1))
#Without using built-in functions
for i in range(len(list1)-1):
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j+1]: 
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)