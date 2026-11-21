numbers = [10, 20, 10, 30, 20, 40, 50, 40]

result = []
for n in numbers:
    if n not in result:
        result.append(n)

print("Original:", numbers)
print("Without duplicates:", result)

# Shortcut: dict keeps insertion order
print("Shortcut:", list(dict.fromkeys(numbers)))
