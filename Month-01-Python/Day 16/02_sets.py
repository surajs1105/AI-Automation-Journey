# Day 16 - Topic 2: Sets

# 5.1 Unique elements
numbers = {10, 20, 30, 10, 20}
print(numbers)

# 5.2 Creating sets
a = {10, 20, 30}
print(a, type(a))
empty_set = set()      # correct way
empty_dict = {}        # this is a dict, NOT a set
print(type(empty_set), type(empty_dict))

# 5.3 Adding elements
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
numbers.update([50, 60, 70])
print(numbers)

# 5.4 Removing elements
numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)
numbers.discard(999)   # no error even if absent
try:
    numbers.remove(999)
except KeyError:
    print("remove() raised KeyError for a missing element")
print("pop() removed:", numbers.pop())
numbers.clear()
print(numbers)

# 5.5 Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric difference:", A ^ B)

# 5.6 Practical example - attendance management
class_A = {"Amit", "Rahul", "Sneha", "Pooja"}
class_B = {"Rahul", "Pooja", "Kiran", "Rohit"}

common = class_A & class_B
only_A = class_A - class_B
all_students = class_A | class_B

print("Common:", common)
print("Only A:", only_A)
print("All Students:", all_students)
