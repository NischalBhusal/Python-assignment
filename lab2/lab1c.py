#Remove duplicate elements
n = int(input("Enter the number of elements in the list"))
list1 = []
for i in range(n):
    a = int(input("Number"))
    list1.append(a)

#Using built-in methods
print(set(list1))

l2 = []
#Without using built-in methods
for element in list1: 
    if element not in l2 : 
        l2.append(element)
print(l2)