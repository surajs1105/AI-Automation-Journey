# DSA 1: Frequency counter using a dictionary
def frequency_counter(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(frequency_counter([1, 2, 2, 3, 3, 3, 4]))
print(frequency_counter("banana"))
print(frequency_counter(["a", "b", "a", "c", "b", "a"]))
