# Day 22 - GATE OS: sequential vs direct vs indexed file access, demonstrated.
# Fixed-length records so we can jump to a record's byte position.
import os

NAME = "access_demo.txt"
RECORD_SIZE = 16     # each record is padded to 15 chars + newline

students = [("101", "Amit", "85"), ("102", "Rahul", "92"),
            ("103", "Sneha", "78"), ("104", "Priya", "88")]

with open(NAME, "w") as f:
    for roll, name, marks in students:
        f.write(f"{roll},{name},{marks}".ljust(RECORD_SIZE - 1) + "\n")

# 1. SEQUENTIAL access: read records one after another from the start
print("Sequential access (reads every record in order):")
with open(NAME, "r") as f:
    for line in f:
        print(" ", line.strip())

# 2. DIRECT access: jump straight to record k using seek(k * RECORD_SIZE)
print("Direct access (jump to record 3 without reading 1 and 2):")
with open(NAME, "r") as f:
    f.seek(2 * RECORD_SIZE)          # records are numbered from 0
    print(" ", f.readline().strip())

# 3. INDEXED access: an index maps a key (roll no) -> byte position of its record
index = {}
with open(NAME, "r") as f:
    position = 0
    for line in f:
        roll = line.split(",")[0]
        index[roll] = position
        position += len(line)

print("Index:", index)
print("Indexed access (find roll 104 via the index):")
with open(NAME, "r") as f:
    f.seek(index["104"])
    print(" ", f.readline().strip())

os.remove(NAME)
