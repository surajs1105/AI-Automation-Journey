# Day 22 - Appending data ("a" mode preserves existing content)
with open("demo.txt", "w") as f:
    f.write("Welcome to ASCEND 365")

file = open("demo.txt", "a")
file.write("\nPython File Handling")
file.close()

with open("demo.txt", "r") as f:
    print(f.read())
