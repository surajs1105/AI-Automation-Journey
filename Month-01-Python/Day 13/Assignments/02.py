# Create a subject marks dictionary and calculate total and average.
marks = {
    "Python": 85,
    "DSA": 78,
    "DBMS": 90,
    "OS": 82
}

total = sum(marks.values())
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)