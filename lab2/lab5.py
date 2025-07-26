l1 = [1, 2, 3, 4, 5, 6, 7] 
l2 = []

for element in range(len(l1)): 
    if element % 2 == 0 :  
        num = l1[element]  
        count = 0
        for j in range(2, num):  
            if num % j == 0:
                count += 1
        if num > 1 and count == 0:
            l2.append(num)
print(l2)