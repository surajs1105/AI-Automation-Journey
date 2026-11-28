# Day 20 - B: Binary Search - Iterative (best O(1), worst O(log n))
# Requires SORTED data.
numbers = [10, 20, 30, 40, 50, 60, 70]
target = 60

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index:", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1      # search right half
    else:
        high = mid - 1     # search left half
