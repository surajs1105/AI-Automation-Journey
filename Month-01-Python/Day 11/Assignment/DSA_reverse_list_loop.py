def reverse_list(numbers):
    result = []
    for i in range(len(numbers) - 1, -1, -1):
        result.append(numbers[i])
    return result

print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]