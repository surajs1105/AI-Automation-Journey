# DSA 1: Linear search  (best O(1), worst O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


data = [64, 25, 12, 22, 11, 90]
for t in (22, 90, 100):
    idx = linear_search(data, t)
    print(f"Target {t}:", f"found at index {idx}" if idx != -1 else "not found")
