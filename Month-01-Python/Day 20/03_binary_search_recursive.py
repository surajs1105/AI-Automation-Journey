# Day 20 - C: Recursive Binary Search
def binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)
    else:
        return binary_search(arr, low, mid - 1, target)


numbers = [10, 20, 30, 40, 50, 60]
result = binary_search(numbers, 0, len(numbers) - 1, 50)
print(result)
