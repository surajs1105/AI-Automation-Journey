# Day 21 - GATE complexity examples, verified by counting operations
for n in (8, 16, 32):
    # Example 1: one loop -> O(n)
    c1 = 0
    for i in range(n):
        c1 += 1

    # Example 2: i *= 2 -> O(log n)
    c2, i = 0, 1
    while i < n:
        i *= 2
        c2 += 1

    # Example 3: j in range(i) -> n(n-1)/2 -> O(n^2)
    c3 = 0
    for i in range(n):
        for j in range(i):
            c3 += 1

    # Example 4: inner loop fixed at 5 -> 5n -> O(n)
    c4 = 0
    for i in range(n):
        for j in range(5):
            c4 += 1

    print(f"n={n:<3} Ex1={c1:<4} Ex2={c2:<2} Ex3={c3:<4} Ex4={c4:<4}")
