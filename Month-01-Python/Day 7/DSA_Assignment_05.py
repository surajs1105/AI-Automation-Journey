# Selection Sort in Descending Order
numbers = [18, 5, 25, 10, 2]

for i in range(len(numbers)):
    max_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[max_index]:
            max_index = j
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print("Sorted array in descending order:", numbers)