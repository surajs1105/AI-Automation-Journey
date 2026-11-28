# DSA 1: Difference between Bubble Sort and Selection Sort
#
# BUBBLE SORT
#  - Repeatedly compares ADJACENT elements and swaps them if out of order.
#  - Large elements "bubble" to the end after each pass.
#  - Many swaps (up to O(n^2)).
#  - Best case O(n) with early exit (already sorted), worst O(n^2).
#  - Stable.
#
# SELECTION SORT
#  - Each pass FINDS the minimum of the unsorted part and swaps it into place.
#  - At most n-1 swaps (O(n)) but always n(n-1)/2 comparisons.
#  - O(n^2) in best, average and worst cases (no early exit).
#  - Not stable in the usual swap-based form.
#
# Demo: count swaps and comparisons on the same data.

def bubble_stats(arr):
    arr = arr[:]
    comps = swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comps, swaps


def selection_stats(arr):
    arr = arr[:]
    comps = swaps = 0
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            comps += 1
            if arr[j] < arr[m]:
                m = j
        if m != i:
            arr[i], arr[m] = arr[m], arr[i]
            swaps += 1
    return comps, swaps


data = [8, 7, 6, 5, 4, 3, 2, 1]
print("Data:", data)
print("Bubble    (comparisons, swaps):", bubble_stats(data))
print("Selection (comparisons, swaps):", selection_stats(data))
