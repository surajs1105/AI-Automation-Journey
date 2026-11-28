# Day 20 - Project: Student Marks Management System (Step 2)
# Added today: search_student(), calculate_average(), display_ranking()

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


def calculate_average():
    total = 0
    for student in students:
        total += student["marks"]
    average = total / len(students)
    print("Average Marks:", average)


def display_ranking():
    ranked_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    for rank, student in enumerate(ranked_students, start=1):
        print(rank, student["name"], student["marks"])


search_student(102)
search_student(999)
calculate_average()
display_ranking()
