def reverse_list(numbers):
    result = []

    for i in range(len(numbers) - 1, -1, -1):
        result.append(numbers[i])

    return result


print(reverse_list([10, 20, 30, 40]))