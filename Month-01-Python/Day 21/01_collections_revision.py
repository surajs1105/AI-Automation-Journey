# Day 21 - Python collections revision

# List: ordered, mutable, duplicates allowed
numbers = [10, 20, 30]
numbers.append(40)
print("List      :", numbers)

# Tuple: ordered, immutable, duplicates allowed
coordinates = (10, 20)
x, y = coordinates                      # unpacking
print("Tuple     :", coordinates, "x =", x, "y =", y)

# Set: unordered, mutable, NO duplicates
unique_numbers = {10, 20, 30, 10, 20}
print("Set       :", unique_numbers)

# Dictionary: key-value pairs, insertion-ordered, keys unique
student = {"name": "Amit", "marks": 85}
student["branch"] = "Computer"
print("Dictionary:", student)
print("get() safe:", student.get("city", "Not Available"))

# Quick comparison
print("\nCollection  Ordered  Mutable  Duplicates")
print("List        Yes      Yes      Yes")
print("Tuple       Yes      No       Yes")
print("Set         No       Yes      No")
print("Dictionary  Yes*     Yes      Keys unique   (*insertion order)")
