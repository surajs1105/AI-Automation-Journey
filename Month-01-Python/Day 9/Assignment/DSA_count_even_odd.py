def count_even_odd(numbers):
    even = 0
    odd = 0
    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

e, o = count_even_odd([10, 15, 22, 7, 8, 3])
print("Even:", e)   # 3
print("Odd:", o)    # 3