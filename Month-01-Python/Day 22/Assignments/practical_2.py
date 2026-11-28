# Practical 2: Display all saved student records
# Creates a few sample records first if students.txt does not exist yet.
import os

if not os.path.exists("students.txt"):
    with open("students.txt", "w") as f:
        f.write("101,Amit,85\n102,Rahul,92\n103,Sneha,78\n")

print(f"{'Roll':<8}{'Name':<10}{'Marks':<6}")
print("-" * 24)
with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks = [x.strip() for x in line.strip().split(",")]
        print(f"{roll:<8}{name:<10}{marks:<6}")
