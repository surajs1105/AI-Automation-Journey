def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
result = sum_to_n(5)
print("Sum: ",result)  
# One-liner alternative: n * (n + 1) // 2