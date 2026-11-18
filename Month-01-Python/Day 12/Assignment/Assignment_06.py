# Check anagrams without sorted()
def are_anagrams(a, b):
    if len(a) != len(b):
        return False

    for ch in a:
        if a.count(ch) != b.count(ch):
            return False

    return True


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))