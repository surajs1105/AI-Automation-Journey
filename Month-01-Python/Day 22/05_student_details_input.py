# Day 22 - Practical example: student details saved with append mode
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

with open("students.txt", "a") as file:
    file.write(f"{roll_no}, {name}, {marks}\n")

print("Student record saved successfully!")
