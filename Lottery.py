import random
lottery_numbers = random.sample(range(1, 101), 15)
print("Generated Lottery Numbers:", lottery_numbers)

random.shuffle(lottery_numbers)
group1 = lottery_numbers[:5]
group2 = lottery_numbers[5:10]
group3 = lottery_numbers[10:]

print("\nGroup 1:", group1)
print("Group 2:", group2)
print("Group 3:", group3)

sum1 = sum(group1)
sum2 = sum(group2)
sum3 = sum(group3)

print("\nSum of Group 1:", sum1)
print("Sum of Group 2:", sum2)
print("Sum of Group 3:", sum3)

if sum1 > sum2 and sum1 > sum3:
    winner = "Group 1"
elif sum2 > sum1 and sum2 > sum3:
    winner = "Group 2"
elif sum3 > sum1 and sum3 > sum2:
    winner = "Group 3"
else:
    winner = "It's a tie!"

print("\nWinner:", winner)