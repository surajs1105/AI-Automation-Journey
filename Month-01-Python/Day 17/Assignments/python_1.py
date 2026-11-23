# Python 1: Dictionary of five students - update marks using update()
students = {"Amit": 85, "Rahul": 70, "Sneha": 95, "Pooja": 60, "Kiran": 78}
print("Before:", students)

students.update({"Rahul": 82, "Pooja": 68})   # updates existing keys
print("After :", students)
