# Store five students and their marks. Find the student with the highest marks.
students = {
    "Amit": 78,
    "Rahul": 85,
    "Sneha": 92,
    "Priya": 88,
    "Rohit": 75
}

highest_student = max(students, key=students.get)

print("Topper:", highest_student)
print("Marks:", students[highest_student])