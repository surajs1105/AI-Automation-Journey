# Python 4: Sort student records by marks in descending order
students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 90},
    {"name": "Sneha", "marks": 85},
    {"name": "Priya", "marks": 65},
    {"name": "Kiran", "marks": 78},
]

ranked = sorted(students, key=lambda s: s["marks"], reverse=True)

for rank, s in enumerate(ranked, start=1):
    print(rank, s["name"], s["marks"])
