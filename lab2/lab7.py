l1 = []
for i in range(3): 
    print(f"Enter the x-coordinate for the tuple {i+1}")
    x = int(input())
    print(f"Enter the y-coordinate for the tuple {i+1}")
    y = int(input())
    l1.append((x, y))
if((l1[1][1]-l1[0][1])*(l1[2][0]-l1[0][0])==(l1[1][0]-l1[0][0])*(l1[2][1]-l1[0][1])):
    print("The given points are collinear")
else: 
    print("The given points are not collinear")