#Merge two lists and then remove all the common elements
l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6, 7]
l3 = l1 + l2
print("Merged list :", l3)
l4 = l3.copy()
for element in l4 : 
    if element in l1 and element in l2 : 
        l3.remove(element)
print(l3)
#Alternative method
print(list(set(l1).symmetric_difference(set(l2))))