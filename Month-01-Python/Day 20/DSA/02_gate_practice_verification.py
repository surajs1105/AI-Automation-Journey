# Day 20 - GATE practice problems Q3 and Q4, verified by counting
import math

# Q3: i = i * 3 until i >= n  -> O(log n)  (log base 3, constant factor ignored)
for n in (10, 100, 1000, 10**6):
    i, steps = 1, 0
    while i < n:
        i = i * 3
        steps += 1
    print(f"Q3 n={n:<8} steps={steps:<3} log3(n)={math.log(n, 3):.2f}")

# Q4: for j in range(i) inside for i in range(n) -> 0+1+...+(n-1) = n(n-1)/2 -> O(n^2)
for n in (5, 10, 100):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    print(f"Q4 n={n:<4} iterations={count:<5} n(n-1)/2={n * (n - 1) // 2}")
