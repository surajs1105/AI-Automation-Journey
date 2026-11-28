# Python 4: Read a file line by line
with open("sample.txt", "w") as f:
    f.write("Welcome to ASCEND 365\nPython File Handling\nDay 22\n")

with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")        # strip() removes the \n
