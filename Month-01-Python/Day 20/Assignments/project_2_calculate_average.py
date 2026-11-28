# Project 2: calculate_average()
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]


def calculate_average():
    if not students:
        print("No students")
        return
    total = 0
    for student in students:
        total += student["marks"]
    average = total / len(students)
    print("Average Marks:", average)


calculate_average()
