# Day 17 - Python: enumerate(), zip(), sorted()

# 5.1 enumerate()
names = ["Amit", "Rahul", "Sneha"]
for i in range(len(names)):          # without enumerate
    print(i, names[i])

for index, name in enumerate(names):  # with enumerate
    print(index, name)

for index, name in enumerate(names, start=1):
    print(index, name)

# 5.2 zip()
marks = [85, 90, 95]
for name, mark in zip(names, marks):
    print(name, mark)

# 5.3 sorted()
marks = [85, 45, 95, 65, 75]
print(sorted(marks))
print(sorted(marks, reverse=True))

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 95},
    {"name": "Sneha", "marks": 75},
]
result = sorted(students, key=lambda student: student["marks"], reverse=True)
for student in result:
    print(student)
