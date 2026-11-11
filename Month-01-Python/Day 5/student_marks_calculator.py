subject1 = float(input("Enter the marks of First Subject: "))
subject2 = float(input("Enter the marks of Second Subject: "))
subject3 = float(input("Enter the marks of Third Subject: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100
print("Total: ",total)
print("Percentage: ",percentage)

if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
  print("PASS")
else:
  print("FAIL")

  

