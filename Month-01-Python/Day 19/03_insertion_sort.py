# Day 19 - Part C: Insertion Sort
# Best O(n) | Average O(n^2) | Worst O(n^2)
numbers = [5, 2, 4, 1, 3]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key

print(numbers)
