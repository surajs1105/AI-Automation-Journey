# Python 5: Highest and lowest marks from a student dictionary
marks = {"Amit": 75, "Rahul": 90, "Sneha": 85, "Priya": 65, "Kiran": 78}

top_student = max(marks, key=marks.get)      # key with the largest value
low_student = min(marks, key=marks.get)

print("Highest:", top_student, marks[top_student])
print("Lowest :", low_student, marks[low_student])
