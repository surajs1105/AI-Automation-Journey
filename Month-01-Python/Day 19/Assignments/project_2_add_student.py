# Project 2: Implement add_student()
students = []


def add_student(roll_no, name, marks):
    # Basic validation: no duplicate roll numbers, marks within 0-100
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"Roll number {roll_no} already exists - not added")
            return False
    if not (0 <= marks <= 100):
        print("Marks must be between 0 and 100 - not added")
        return False

    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    return True


add_student(101, "Amit", 85)
add_student(102, "Rahul", 92)
add_student(101, "Duplicate", 50)   # rejected
add_student(103, "Sneha", 150)      # rejected
add_student(103, "Sneha", 78)
print(students)
