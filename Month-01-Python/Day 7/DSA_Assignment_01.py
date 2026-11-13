# Linear Search Algorithm Implementation
numbers = [10, 15, 20, 25, 30, 35]
target = 25


comparisons = 0
for index in range(len(numbers)):
	comparisons += 1
	if number == target:
		print(f"{target} found at index {index} after {comparisons} comparisons")
		break
else:
	print(f"{target} not found after {comparisons} comparisons")
