# Day 19 - Part A: Bubble Sort
# Best O(n) with early exit | Average O(n^2) | Worst O(n^2)
numbers = [5, 3, 8, 1, 2]
n = len(numbers)

for i in range(n):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
