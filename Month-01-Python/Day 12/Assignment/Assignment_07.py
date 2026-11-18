# Find the first non-repeating character
def first_non_repeating(text):
    for ch in text:
        if text.count(ch) == 1:
            return ch

    return None


print(first_non_repeating("programming"))
print(first_non_repeating("aabbcc"))