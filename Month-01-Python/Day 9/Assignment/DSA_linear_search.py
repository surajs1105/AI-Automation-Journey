def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40, 50], 30))   # 2
print(linear_search([10, 20, 30, 40, 50], 99))   # -1