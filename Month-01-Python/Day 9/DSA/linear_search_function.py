def linear_search(numbers, target):
  for i in range(len(numbers)):
    if numbers[i] == target:
      return i

  return "not found"

values = [10, 20, 30, 40, 50]

print(linear_search(values, 31))