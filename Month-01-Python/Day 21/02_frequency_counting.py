# Day 21 - Dictionary frequency counting
# Dictionary lookup: average O(1), worst O(n)  ->  this loop is O(n) expected
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)
