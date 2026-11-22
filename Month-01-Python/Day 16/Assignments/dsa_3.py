# DSA 3: Hashing and hash collision with my own example
#
# Hashing: a hash function converts a key into an integer, which is used to
# decide where the value is stored in a hash table (an array of "buckets").
#
# Example: table size = 7, hash function h(key) = key % 7
#   Roll 15 -> 15 % 7 = 1  -> stored at index 1
#   Roll 22 -> 22 % 7 = 1  -> also index 1  => COLLISION
#   Roll 10 -> 10 % 7 = 3  -> stored at index 3
#
# Collision: two different keys map to the same index.
# Resolved by:
#   1. Chaining        - each index holds a list of all keys that map there.
#   2. Open addressing - probe for the next free slot (linear/quadratic/double hashing).

TABLE_SIZE = 7

def h(key):
    return key % TABLE_SIZE

# --- Chaining demo ---
table = [[] for _ in range(TABLE_SIZE)]

def insert(key, value):
    table[h(key)].append((key, value))

def search(key):
    for k, v in table[h(key)]:
        if k == key:
            return v
    return None

insert(15, "Amit")
insert(22, "Rahul")   # collides with 15 at index 1
insert(10, "Sneha")

for i, bucket in enumerate(table):
    print(i, bucket)

print("Search 22:", search(22))
print("Search 10:", search(10))
