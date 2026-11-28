# DSA 2: Sort student records by marks
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]

print("Ascending:")
for s in sorted(students, key=lambda s: s["marks"]):
    print(s["name"], s["marks"])

print("Descending:")
for s in sorted(students, key=lambda s: s["marks"], reverse=True):
    print(s["name"], s["marks"])
