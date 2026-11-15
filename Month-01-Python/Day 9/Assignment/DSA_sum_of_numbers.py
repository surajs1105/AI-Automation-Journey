def list_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
sum = [10, 20, 30, 40]
print(list_sum(sum))   # 100