# Project 3: Implement display_students()
students = []


def add_student(roll_no, name, marks):
    students.append({"roll_no": roll_no, "name": name, "marks": marks})


def display_students():
    if not students:
        print("No students to display")
        return
    print(f"{'Roll No':<10}{'Name':<12}{'Marks':<6}")
    print("-" * 28)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<12}{s['marks']:<6}")


display_students()          # empty case
add_student(101, "Amit", 85)
add_student(102, "Rahul", 92)
add_student(103, "Sneha", 78)
display_students()
