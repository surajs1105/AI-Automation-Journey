# Practical 1: Program to store student names in a file
names = ["Amit", "Rahul", "Sneha", "Priya", "Kiran"]    # or collect with input()

with open("student_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print(f"{len(names)} student names saved to student_names.txt")
