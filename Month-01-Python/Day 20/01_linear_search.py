# Day 20 - A: Linear Search (best O(1), average O(n), worst O(n))
numbers = [12, 25, 37, 48, 59]
target = 37

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        break
else:   # runs only if the loop finished without break
    print("Element not found")
