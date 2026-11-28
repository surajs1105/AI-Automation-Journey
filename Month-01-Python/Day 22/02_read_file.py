# Day 22 - Reading data from a file
# (creates demo.txt first so this script runs on its own)
with open("demo.txt", "w") as f:
    f.write("Welcome to ASCEND 365\nPython File Handling\nThird line\n")

file = open("demo.txt", "r")
content = file.read()             # reads the entire file
print(content)
file.close()

# Three useful reading methods
file = open("demo.txt", "r")
print("readline() :", repr(file.readline()))     # one line
print("readlines():", file.readlines())          # remaining lines as a list
file.close()
