# DSA 3: Calculate the average marks of students
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]

if students:
    total = sum(s["marks"] for s in students)
    print("Total  :", total)
    print("Average:", total / len(students))
else:
    print("No students")
