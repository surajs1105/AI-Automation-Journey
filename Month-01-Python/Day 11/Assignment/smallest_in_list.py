def smallest(numbers):
    small = numbers[0]
    for n in numbers:
        if n < small:
            small = n
    return small

print(smallest([45, 12, 78, 23, 9, 56]))   # 9