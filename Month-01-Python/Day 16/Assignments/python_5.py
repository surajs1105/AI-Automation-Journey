# Python 5: Nested dictionary for five students - name, branch, marks
students = {
    1: {"name": "Amit",  "branch": "CO", "marks": 85},
    2: {"name": "Rahul", "branch": "IT", "marks": 90},
    3: {"name": "Sneha", "branch": "CO", "marks": 95},
    4: {"name": "Pooja", "branch": "EE", "marks": 72},
    5: {"name": "Kiran", "branch": "ME", "marks": 78},
}

for roll_no, d in students.items():
    print("Roll No:", roll_no)
    print("Name   :", d["name"])
    print("Branch :", d["branch"])
    print("Marks  :", d["marks"])
    print("-" * 20)
