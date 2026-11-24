# Day 18 - Sorting algorithms side by side, with comparison counts
# Bubble (optimized), Selection, Insertion

def bubble_sort(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:          # early exit -> best case O(n)
            break
    return arr, comparisons


def selection_sort(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons


def insertion_sort(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons


cases = {
    "Already sorted": [1, 2, 3, 4, 5, 6, 7, 8],
    "Reverse sorted": [8, 7, 6, 5, 4, 3, 2, 1],
    "Random":         [5, 3, 8, 1, 7, 2, 6, 4],
}

for label, data in cases.items():
    print(label, data)
    for name, fn in (("Bubble", bubble_sort),
                     ("Selection", selection_sort),
                     ("Insertion", insertion_sort)):
        result, count = fn(data)
        print(f"  {name:<10} -> {result}  comparisons: {count}")
