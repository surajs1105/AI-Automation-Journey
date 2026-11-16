numbers = [10, 20, 30, 20, 40, 10]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate:", numbers[i])