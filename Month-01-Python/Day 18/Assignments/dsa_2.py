# DSA 2: Binary search  (best O(1), worst O(log n)) - array must be sorted
def binary_search(arr, target):
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
for t in (50, 10, 70, 35):
    idx = binary_search(data, t)
    print(f"Target {t}:", f"found at index {idx}" if idx != -1 else "not found")
