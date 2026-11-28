# Project 2: add_student() with permanent storage
def add_student(roll=None, name=None, marks=None):
    if roll is None:                       # interactive mode
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Record Saved Successfully!")


# Demo with three students (replace with add_student() to type your own)
add_student(101, "Amit", 85)
add_student(102, "Rahul", 92)
add_student(103, "Sneha", 78)
