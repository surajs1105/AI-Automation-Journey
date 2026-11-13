numbers = [40, 10, 30, 20, 50]

for i in range(len(numbers) - 1):
	for j in range(len(numbers) - 1):
		if numbers[j] > numbers[j + 1]:
			numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted numbers:", numbers)
