# Day 19 - Mini Project: Student Marks Management System (Step 1)
# Features planned: add, display, total/average, grades, highest/lowest,
# search by roll number, sort by marks, save to file.
# Today: create student records (add + display).

students = []


def add_student(roll_no, name, marks):
    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
    }
    students.append(student)


def display_students():
    for student in students:
        print(student["roll_no"], student["name"], student["marks"])


add_student(101, "Amit", 85)
add_student(102, "Rahul", 92)
add_student(103, "Sneha", 78)

# Your task: add two more students independently
add_student(104, "Priya", 88)
add_student(105, "Kiran", 69)

display_students()
