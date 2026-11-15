def check_number(n):
  if n > 0:
    return "Positive"
  elif n < 0:
    return "Negative"  
  else:
    return "Zero"

print(check_number(7))
print(check_number(0))
print(check_number(-3))
