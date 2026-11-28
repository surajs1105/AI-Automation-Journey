# Python 1: Create a text file using Python
# "x" creates a new file and fails if it exists; "w" creates or overwrites.
with open("my_first_file.txt", "w") as file:
    file.write("This file was created using Python.\n")

print("File created: my_first_file.txt")
