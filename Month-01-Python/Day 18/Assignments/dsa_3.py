# DSA 3: Bubble sort  (worst O(n^2), best O(n) with early exit)
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


data = [64, 34, 25, 12, 22, 11, 90]
print("Before:", data)
print("After :", bubble_sort(data))
