numbers = [10, 20, 30, 40, 50]

target = 30
found = False

for i in range(len(numbers)):
  if numbers[i] == target:
    print("Element is found at index ", i)
    found = True
    break

if not found:
  print("Element not found")