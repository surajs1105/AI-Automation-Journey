# Day 16 - Topic 3: Dictionaries

# 6.1 Key-value pairs
student = {"name": "Suraj", "age": 24, "branch": "Computer", "marks": 85}
print(student)

# 6.2 Accessing values
print(student["name"])
print(student["marks"])
print(student.get("age"))
print(student.get("city", "Not Available"))
# student["city"] would raise KeyError; get() returns None / default instead

# 6.3 Adding and updating
student = {"name": "Suraj", "marks": 80}
student["branch"] = "Computer"
student["marks"] = 90
print(student)

# 6.4 Removing elements
student.pop("marks")
print(student)

student = {"name": "Suraj", "marks": 90, "branch": "Computer"}
print("keys:", student.keys())
print("values:", student.values())
print("items:", student.items())
student.update({"age": 24})
print("popitem:", student.popitem())   # removes last inserted pair
student.clear()
print(student)

# 6.5 Iterating
student = {"name": "Suraj", "age": 24, "marks": 85}
for key, value in student.items():
    print(key, ":", value)

# 6.6 Nested dictionaries
students = {
    101: {"name": "Amit", "marks": 85},
    102: {"name": "Rahul", "marks": 90},
    103: {"name": "Sneha", "marks": 95},
}
print(students[102]["name"])
print(students[103]["marks"])

# 6.7 Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares = {n: n * n for n in numbers}
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_squares = {n: n * n for n in numbers if n % 2 == 0}
print(even_squares)
