# Algorithm Comparison
# Perform Bubble Sort and Selection Sort.

# Record:
# - Final sorted list.
# - Number of comparisons.
# - Number of swaps.

numbers = [40, 10, 30, 20, 50]
#Bubble Sort
bubble_numbers = numbers.copy()
bubble_comparisons = 0  
bubble_swaps = 0
for i in range(len(bubble_numbers)):
    for j in range(len(bubble_numbers) - 1):
        bubble_comparisons += 1
        if bubble_numbers[j] > bubble_numbers[j + 1]:
            bubble_numbers[j], bubble_numbers[j + 1] = (
                bubble_numbers[j + 1],
                bubble_numbers[j],
            )
            bubble_swaps += 1

print("Bubble Sort - Final sorted list:", bubble_numbers)
print("Bubble Sort - Number of comparisons:", bubble_comparisons) 
print("Bubble Sort - Number of swaps:", bubble_swaps)

#Selection Sort
selection_numbers = numbers.copy()  
selection_comparisons = 0
selection_swaps = 0
for i in range(len(selection_numbers)):
    min_index = i
    for j in range(i + 1, len(selection_numbers)):
        selection_comparisons += 1
        if selection_numbers[j] < selection_numbers[min_index]:
            min_index = j
    if min_index != i:
        selection_numbers[i], selection_numbers[min_index] = (
            selection_numbers[min_index],
            selection_numbers[i],
        )
        selection_swaps += 1

print("Selection Sort - Final sorted list:", selection_numbers)
print("Selection Sort - Number of comparisons:", selection_comparisons)
print("Selection Sort - Number of swaps:", selection_swaps)   