import random
length = random.choice([10, 11])
list1 = [random.randint(1, 10) for i in range(length)]
list1.sort()
print(list1)
print("Mean :", sum(list1)/len(list1))
if(len(list1) % 2 ==0): 
    n1 = list1[(len(list1)//2)-1]
    n2 = list1[(len(list1)//2)]
    print("Median :", (n1+n2)/2)
else: 
    print("Median :", list1[len(list1)//2])
unique_list1 = []
for element in list1 : 
    if element not in unique_list1: 
        unique_list1.append(element)
freq_list = []
for element in unique_list1 : 
    freq_list.append(list1.count(element))
if max(freq_list) > 1 : 
    print("Mode :", unique_list1[freq_list.index(max(freq_list))], "Frequency :", max(freq_list))
else : 
    print("Mode does not exist")