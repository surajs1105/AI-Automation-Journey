# Day 20 - Python built-in sorting: sorted() vs sort()
numbers = [50, 20, 40, 10, 30]
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print("Original unchanged:", numbers)

# sort() modifies the original list and returns None
result = numbers.sort()
print("sort() returned:", result)
print("Original now   :", numbers)
