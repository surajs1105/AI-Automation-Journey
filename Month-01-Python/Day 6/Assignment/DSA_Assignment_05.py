
numbers = [50, 20, 40, 10, 30]

# -------------------------
# BUBBLE SORT
# -------------------------

bubble = numbers.copy()

bubble_comparisons = 0
bubble_swaps = 0

n = len(bubble)

for i in range(n - 1):
    for j in range(n - i - 1):

        bubble_comparisons += 1

        if bubble[j] > bubble[j + 1]:

            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

            bubble_swaps += 1

print("BUBBLE SORT")
print("Sorted Array:", bubble)
print("Comparisons:", bubble_comparisons)
print("Swaps:", bubble_swaps)


# -------------------------
# SELECTION SORT
# -------------------------

selection = numbers.copy()

selection_comparisons = 0
selection_swaps = 0

n = len(selection)

for i in range(n - 1):

    min_index = i

    for j in range(i + 1, n):

        selection_comparisons += 1

        if selection[j] < selection[min_index]:
            min_index = j

    if min_index != i:

        selection[i], selection[min_index] = selection[min_index], selection[i]

        selection_swaps += 1

print("\nSELECTION SORT")
print("Sorted Array:", selection)
print("Comparisons:", selection_comparisons)
print("Swaps:", selection_swaps)
