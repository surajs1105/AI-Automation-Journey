# Binary Search Algorithm Implementation
numbers = [5, 15, 25, 35, 45, 55, 65, 75]
target = 55

comparisons = 0
low = 0
high = len(numbers) - 1
while low <= high:
    comparisons += 1
    mid = (low + high) // 2
    if numbers[mid] == target:
        print(f"{target} found at index {mid} after {comparisons} comparisons")
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1  

