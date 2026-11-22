# DSA 2: Find duplicate elements in a list using a set
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for x in items:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return duplicates

data = [1, 2, 3, 2, 4, 5, 1, 6, 5]
print("List:", data)
print("Duplicates:", find_duplicates(data))   # O(n) expected time
