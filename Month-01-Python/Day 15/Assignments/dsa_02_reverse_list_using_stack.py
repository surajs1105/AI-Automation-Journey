def reverse_list(numbers):
    stack = []
    for n in numbers:
        stack.append(n)          # push every element

    result = []
    while stack:
        result.append(stack.pop())   # pop gives last-in first-out
    return result

print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
