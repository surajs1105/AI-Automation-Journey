# Day 18 - Part C.2: Binary Search  (best O(1), worst O(log n))
# Requires SORTED data.
numbers = [10, 20, 30, 40, 50, 60]
target = 50

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index:", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
