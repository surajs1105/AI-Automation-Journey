# Day 16 - Practical Mini Project: Student Data Manager

students = {
    1: {"name": "Amit", "marks": 85},
    2: {"name": "Rahul", "marks": 90},
    3: {"name": "Sneha", "marks": 95},
}

for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("----------------")
