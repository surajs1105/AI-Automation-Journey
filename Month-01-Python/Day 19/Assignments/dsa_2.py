# DSA 2: Sort [12, 5, 8, 2, 10] using Insertion Sort (step by step)
numbers = [12, 5, 8, 2, 10]
print("Start:", numbers)

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
    print(f"Pass {i} (insert {key}):", numbers)

print("Sorted:", numbers)

# Expected trace:
# Start : [12, 5, 8, 2, 10]
# Pass 1: [5, 12, 8, 2, 10]   insert 5
# Pass 2: [5, 8, 12, 2, 10]   insert 8
# Pass 3: [2, 5, 8, 12, 10]   insert 2
# Pass 4: [2, 5, 8, 10, 12]   insert 10
