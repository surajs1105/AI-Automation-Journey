marks = {
    "Amit": 78,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95
}

topper = max(marks, key=marks.get)

print("Topper:", topper)
print("Marks:", marks[topper])