# Day 18 - Part C.1: Linear Search  (best O(1), worst O(n))
numbers = [10, 20, 30, 40, 50]
target = 30

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break
