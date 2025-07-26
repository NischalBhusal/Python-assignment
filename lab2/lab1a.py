#Write a program to input n numbers and store them in a list.Find the maximum and minimum number
n = int(input("Enter the number of elements in the list"))
list1 = []
for i in range(n):
    a = int(input("Number"))
    list1.append(a)
print(list1)

#Using built-in functions
print("The maximum number of the list is", max(list1) ,"and the minimum is",  min(list1))

#Without using built-in functions
max = list1[0]
min = list1[0]
for element in list1:
    if element>max:
        max = element
    if element<min: 
        min = element
print(max)
print(min)