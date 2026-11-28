# Python 3: Read the entire contents of a file
with open("sample.txt", "w") as f:           # prepare a sample file
    f.write("Welcome to ASCEND 365\nPython File Handling\nDay 22\n")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)
print("Characters read:", len(content))
