numbers = [5, 10, 15, 20, 25, 30]

target = 25
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")