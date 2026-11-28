# Day 20 - GATE examples: count operations to see the complexity
n = 64

# Example 1 - nested loops: n * n -> O(n^2)
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print("Example 1 (nested loops):", count, "= n^2 =", n * n)

# Example 2 - repeated division: 64 -> 32 -> ... -> 1 = 6 iterations -> O(log n)
m = 64
iterations = 0
while m > 1:
    m = m // 2
    iterations += 1
print("Example 2 (halving):", iterations, "iterations")

# Example 3 - consecutive loops: n + n = 2n -> O(n)
count = 0
for i in range(n):
    count += 1
for j in range(n):
    count += 1
print("Example 3 (consecutive loops):", count, "= 2n =", 2 * n)
