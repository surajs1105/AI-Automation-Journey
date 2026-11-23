# Python 3: enumerate() - student names with roll numbers starting from 1
names = ["Amit", "Rahul", "Sneha", "Pooja", "Kiran"]

for roll_no, name in enumerate(names, start=1):
    print(f"Roll No {roll_no}: {name}")
