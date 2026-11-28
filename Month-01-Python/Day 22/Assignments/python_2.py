# Python 2: Write five lines into a text file
lines = [
    "Line 1: Learning Python file handling",
    "Line 2: Files store data permanently",
    "Line 3: The w mode overwrites content",
    "Line 4: The a mode appends content",
    "Line 5: with open() closes files automatically",
]

with open("five_lines.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

print("Five lines written to five_lines.txt")
