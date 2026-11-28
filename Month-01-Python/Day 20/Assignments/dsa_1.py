# DSA 1: Search for a student using roll number
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]


def find_student(roll_no):
    for student in students:          # linear search, O(n)
        if student["roll_no"] == roll_no:
            return student
    return None


for roll in (103, 999):
    s = find_student(roll)
    print(f"Roll {roll}:", s if s else "Student Not Found")
