a = "Hello how are you right now? I am currently trying to do my homework "
count_dict = {}
for char in a : 
    if char not in count_dict : 
        count_dict.update({char:a.count(char)})
print(count_dict)