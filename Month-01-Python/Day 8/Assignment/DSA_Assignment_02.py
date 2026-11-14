numbers = [45, 12, 78, 23, 9, 56]

smallest = numbers[0]
largest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("Smallest:", smallest)
print("Largest:", largest)