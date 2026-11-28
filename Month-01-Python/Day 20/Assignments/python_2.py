# Python 2: Recursive Binary Search
def binary_search(arr, low, high, target):
    if low > high:          # base case: search space is empty
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)
    else:
        return binary_search(arr, low, mid - 1, target)


data = [10, 20, 30, 40, 50, 60]
for t in (50, 10, 60, 25):
    idx = binary_search(data, 0, len(data) - 1, t)
    print(f"Target {t}:", f"found at index {idx}" if idx != -1 else "not found")
