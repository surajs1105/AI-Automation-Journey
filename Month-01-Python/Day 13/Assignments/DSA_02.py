# Find duplicate elements using a dictionary.
numbers = [5, 10, 15, 10, 20, 5, 30]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Duplicate elements:")

for num, count in frequency.items():
    if count > 1:
        print(num)