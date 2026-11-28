# Project 1: search_student()
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]


def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found")
            print(student)
            return
    print("Student Not Found")


search_student(102)
search_student(999)
