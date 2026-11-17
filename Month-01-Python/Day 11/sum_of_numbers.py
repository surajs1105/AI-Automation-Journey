def calculate_sum(n):
  total = 0

  for i in range(1, n + 1):
    total += i
  return total  

result = calculate_sum(5)
print("Sum: ",result)  