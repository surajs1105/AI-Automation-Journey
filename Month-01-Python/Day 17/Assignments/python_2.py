# Python 2: List of student dictionaries - average marks and highest scorer
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 70},
    {"name": "Sneha", "marks": 95},
    {"name": "Pooja", "marks": 60},
    {"name": "Kiran", "marks": 78},
]

total = sum(s["marks"] for s in students)
average = total / len(students)
topper = max(students, key=lambda s: s["marks"])

print("Average marks:", average)
print("Highest scorer:", topper["name"], "with", topper["marks"])
