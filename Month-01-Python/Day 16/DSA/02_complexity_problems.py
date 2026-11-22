# Day 16 - GATE-style problems from the lesson

# Problem 1 - searching a list: worst case O(n)
numbers = [10, 20, 30, 40, 50]
if 30 in numbers:
    print("Found")

# Problem 2 - dictionary lookup: average case O(1)
student = {101: "Amit", 102: "Rahul", 103: "Sneha"}
print(student[102])

# Problem 3 - frequency count: O(n) expected time
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)
