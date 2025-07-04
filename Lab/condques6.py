positives = negatives = zeros = 0
for _ in range(10):
    num = int(input("Enter a number: "))
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1

print("Positives:", positives)
print("Negatives:", negatives)
print("Zeros:", zeros)
