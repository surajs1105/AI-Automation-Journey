# Day 19 - GATE concept: count the iterations of a dependent nested loop
# T(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2  -> O(n^2)
n = 8
count = 0
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
        count += 1

print("Total iterations:", count)
print("n(n-1)/2 =", n * (n - 1) // 2)   # 28
