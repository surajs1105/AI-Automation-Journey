# Python 4: zip() - combine names, marks and roll numbers into records
names = ["Amit", "Rahul", "Sneha", "Pooja", "Kiran"]
marks = [85, 70, 95, 60, 78]
roll_numbers = [1, 2, 3, 4, 5]

records = {roll: {"name": name, "marks": mark}
           for roll, name, mark in zip(roll_numbers, names, marks)}

for roll, details in records.items():
    print(roll, details)
