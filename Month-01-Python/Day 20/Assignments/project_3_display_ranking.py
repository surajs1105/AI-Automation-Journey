# Project 3: display_ranking()
students = [
    {"roll_no": 101, "name": "Amit", "marks": 85},
    {"roll_no": 102, "name": "Rahul", "marks": 92},
    {"roll_no": 103, "name": "Sneha", "marks": 78},
    {"roll_no": 104, "name": "Priya", "marks": 88},
]


def display_ranking():
    ranked_students = sorted(students, key=lambda x: x["marks"], reverse=True)
    for rank, student in enumerate(ranked_students, start=1):
        print(rank, student["name"], student["marks"])


display_ranking()
