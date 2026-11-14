numbers = [10, -5, 0, 20, -8, 0, 15]

positive = 0
negative = 0
zero = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)