# Find duplicate elements in [5, 10, 15, 10, 20, 5]
numbers = [5, 10, 15, 10, 20, 5]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate:", numbers[i])