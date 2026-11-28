# DSA 4: Why is Merge Sort O(n log n)?
#
# Merge sort splits the list in half, sorts each half recursively, then merges.
#
#   1. DIVIDE: halving n repeatedly until size 1 takes log2(n) levels.
#   2. MERGE : at every level, the merge steps together touch all n elements
#              once, so each level costs O(n).
#
#   Total = (number of levels) x (work per level) = log n x n = O(n log n)
#
# Recurrence: T(n) = 2T(n/2) + O(n)  ->  O(n log n)
# This holds for best, average and worst cases, since splitting and merging
# do not depend on the input order.  Extra space: O(n).

def merge_sort(arr, depth=0, stats=None):
    if stats is None:
        stats = {"levels": 0}
    stats["levels"] = max(stats["levels"], depth)
    if len(arr) <= 1:
        return arr, stats
    mid = len(arr) // 2
    left, _ = merge_sort(arr[:mid], depth + 1, stats)
    right, _ = merge_sort(arr[mid:], depth + 1, stats)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, stats


data = [38, 27, 43, 3, 9, 82, 10, 1]
result, stats = merge_sort(data)
print("Before:", data)
print("After :", result)
print("Levels of splitting:", stats["levels"], "(= log2(8) = 3)")
