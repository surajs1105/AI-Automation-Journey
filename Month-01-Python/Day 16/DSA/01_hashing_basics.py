# Day 16 - DSA: Hashing Fundamentals

# 7.1 Dictionary lookup uses hashing internally
student = {101: "Amit", 102: "Rahul", 103: "Sneha"}
print(student[102])

# 7.2 Hash function (string hashes vary between runs)
print(hash("Suraj"))
print(hash(100))

# 7.3 Collision demo with a simple hash function: index = key % table_size
def simple_hash(key, size):
    return key % size

size = 5
for key in (12, 17, 22):
    print(f"Key {key} -> Index {simple_hash(key, size)}")   # all map to index 2
