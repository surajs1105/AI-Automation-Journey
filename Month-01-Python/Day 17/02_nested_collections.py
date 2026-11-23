# Day 17 - Python: Nested Collections

# 4.1 List inside a dictionary
student = {
    "name": "Amit",
    "subjects": ["Python", "Java", "DBMS"],
    "marks": [85, 90, 78],
}
print(student["subjects"])
print(student["marks"][1])

# 4.2 Dictionary inside a list
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 90},
    {"name": "Sneha", "marks": 95},
]
for s in students:
    print(s["name"], s["marks"])

# 4.3 Average marks
total = 0
for s in students:
    total += s["marks"]
average = total / len(students)
print("Average:", average)
