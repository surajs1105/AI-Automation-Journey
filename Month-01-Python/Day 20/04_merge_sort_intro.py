# Day 20 - Merge Sort (Divide and Conquer), O(n log n) in all cases
# Follows the lesson example: [8, 4, 2, 6] -> [8,4] [2,6] -> [8] [4] [2] [6]
#                              -> [4, 8] [2, 6] -> [2, 4, 6, 8]

def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}Divide: {arr}")
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    print(f"{indent}Merge : {left} + {right} -> {merged}")
    return merged


print("Final:", merge_sort([8, 4, 2, 6]))
