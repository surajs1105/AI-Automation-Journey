# Python 3: Five students and marks - display those scoring above 75
marks = {"Amit": 85, "Rahul": 70, "Sneha": 95, "Pooja": 60, "Kiran": 78}

print("Students scoring above 75:")
for name, score in marks.items():
    if score > 75:
        print(f"{name}: {score}")
