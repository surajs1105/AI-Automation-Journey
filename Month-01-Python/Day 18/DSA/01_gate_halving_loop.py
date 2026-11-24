# Day 18 - GATE practice: repeated halving -> O(log n)
n = 16
iterations = 0
while n > 1:
    n = n // 2
    iterations += 1
print("Iterations:", iterations)   # 16 -> 8 -> 4 -> 2 -> 1 = 4
