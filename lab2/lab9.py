import random
s = set()
for i in range(10) : 
    s.add(random.randint(1, 50))
print(s)
s.remove(max(s))
s.remove(min(s))
print(s)