# Python 1: Iterative Binary Search
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [10, 20, 30, 40, 50, 60, 70]
for t in (60, 10, 70, 35):
    idx = binary_search_iterative(data, t)
    print(f"Target {t}:", f"found at index {idx}" if idx != -1 else "not found")
