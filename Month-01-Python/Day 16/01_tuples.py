# Day 16 - Topic 1: Tuples

# 4.1 What is a tuple?
student = ("Suraj", 24, 8.02)
print(student)
print(type(student))

# 4.2 Creating tuples
a = ()                      # empty
numbers = (10, 20, 30, 40)  # integers
student = ("Suraj", 24, 8.02)
data = 10, 20, 30           # without parentheses
single = (10,)              # single-element needs a comma

x = (10)
y = (10,)
print(type(x))  # int
print(type(y))  # tuple

# 4.3 Accessing elements
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[2])
print(numbers[-1])

# 4.4 Slicing
print(numbers[1:4])
print(numbers[::-1])

# 4.5 Methods
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
print(numbers.index(20))

# 4.6 Immutability
numbers = (10, 20, 30)
try:
    numbers[0] = 100
except TypeError as e:
    print("TypeError:", e)

numbers = (100,) + numbers[1:]   # create a new tuple instead
print(numbers)

# 4.7 Tuple unpacking
student = ("Suraj", "CO", 2026)
name, branch, year = student
print(name)
print(branch)
print(year)
