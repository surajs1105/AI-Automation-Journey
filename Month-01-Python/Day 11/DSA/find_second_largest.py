def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[-2]


print(second_largest([10, 25, 40, 15, 40]))