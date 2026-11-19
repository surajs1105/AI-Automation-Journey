student_marks = {
    "Python": 85,
    "DSA": 78,
    "DBMS": 90
}

for subject, marks in student_marks.items():
    print(subject, ":", marks)

total = sum(student_marks.values())
average = total / len(student_marks)

print("Total:", total)
print("Average:", average)