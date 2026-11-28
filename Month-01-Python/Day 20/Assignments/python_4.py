# Python 4: Merge Sort - implementation plus complete working
#
# 1. DIVIDE   : split the list into two halves until each part has 1 element
#               (a single element is already sorted).
# 2. CONQUER  : sort each half recursively.
# 3. COMBINE  : merge two sorted halves by repeatedly taking the smaller front element.
#
# [38, 27, 43, 3] -> [38, 27] [43, 3] -> [38] [27] [43] [3]
# merge -> [27, 38] [3, 43] -> merge -> [3, 27, 38, 43]
#
# Time: O(n log n) always (log n levels x O(n) merge per level). Space: O(n).

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # <= keeps the sort stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


data = [38, 27, 43, 3, 9, 82, 10]
print("Before:", data)
print("After :", merge_sort(data))
