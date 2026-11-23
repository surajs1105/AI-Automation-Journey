# Python 5: Sort student dictionaries by marks (descending) using sorted() + lambda
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 70},
    {"name": "Sneha", "marks": 95},
    {"name": "Pooja", "marks": 60},
    {"name": "Kiran", "marks": 78},
]

ranked = sorted(students, key=lambda s: s["marks"], reverse=True)
for rank, s in enumerate(ranked, start=1):
    print(rank, s["name"], s["marks"])
