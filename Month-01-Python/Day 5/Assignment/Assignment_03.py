m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print("Total Marks:", total)
print("Percentage:", percentage)

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")