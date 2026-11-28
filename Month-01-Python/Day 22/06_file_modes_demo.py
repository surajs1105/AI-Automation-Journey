# Day 22 - File modes: r, w, a, x, r+
import os

NAME = "modes_demo.txt"
if os.path.exists(NAME):
    os.remove(NAME)

# "r" requires an existing file
try:
    open(NAME, "r")
except FileNotFoundError:
    print("r  : FileNotFoundError (file does not exist yet)")

# "x" creates a new file, fails if it exists
with open(NAME, "x") as f:
    f.write("created with x\n")
print("x  : file created")
try:
    open(NAME, "x")
except FileExistsError:
    print("x  : FileExistsError (file already exists)")

# "a" appends, keeps old content
with open(NAME, "a") as f:
    f.write("added with a\n")
print("a  :", open(NAME).read().splitlines())

# "r+" reads and writes (does not truncate)
with open(NAME, "r+") as f:
    first = f.readline()
    f.write("added with r+\n")        # writes at the current position, no truncation
                                   # (here the end: the read buffered the small file)
print("r+ :", open(NAME).read().splitlines())

# "w" overwrites everything
with open(NAME, "w") as f:
    f.write("only this remains\n")
print("w  :", open(NAME).read().splitlines())

os.remove(NAME)                        # clean up
