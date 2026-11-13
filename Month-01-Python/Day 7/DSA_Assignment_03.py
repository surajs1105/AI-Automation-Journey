# DSA Assignment 03: Bubble Sort and Selection Sort
numbers = [5, 3, 4, 1]

# Bubble Sort: perform one complete pass through adjacent elements.
bubble_numbers = numbers.copy()
for index in range(len(bubble_numbers) - 1):
	if bubble_numbers[index] > bubble_numbers[index + 1]:
		bubble_numbers[index], bubble_numbers[index + 1] = (
			bubble_numbers[index + 1],
			bubble_numbers[index],
		)

print("Bubble Sort after first pass:", bubble_numbers)

# Selection Sort: find the smallest element and place it at the beginning.
selection_numbers = numbers.copy()
smallest_index = 0
for index in range(1, len(selection_numbers)):
	if selection_numbers[index] < selection_numbers[smallest_index]:
		smallest_index = index

selection_numbers[0], selection_numbers[smallest_index] = (
	selection_numbers[smallest_index],
	selection_numbers[0],
)

print("Selection Sort after first pass:", selection_numbers)
