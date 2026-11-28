# Day 22 - Best practice: with open() closes the file automatically,
# even if an exception occurs inside the block.
with open("demo.txt", "w") as file:
    file.write("Learning Python File Handling")

with open("demo.txt", "r") as file:
    print(file.read())

print("File closed automatically:", file.closed)    # True
