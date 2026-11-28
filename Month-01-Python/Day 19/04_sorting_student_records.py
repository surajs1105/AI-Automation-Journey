# Day 19 - Part D: Sorting student records
students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 90},
    {"name": "Sneha", "marks": 85},
    {"name": "Priya", "marks": 65},
]

students.sort(key=lambda student: student["marks"], reverse=True)

for student in students:
    print(student["name"], student["marks"])
