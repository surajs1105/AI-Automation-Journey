def largest_num(a, b, c):
  if a > b and a > c:
    return a 
  elif b > a and b > c:
    return b
  else:
    return c

print(largest_num(22, 56, 10), "is largest")