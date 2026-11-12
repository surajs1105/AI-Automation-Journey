Phy = float(input("Enter the Marks of Physics: "))
Chem = float(input("Enter the Marks of Chemistry: "))
Maths = float(input("Enter the marks of Maths: "))

total = Phy + Chem + Maths
percentage = ((Phy + Chem + Maths) / 300) * 100

print("Total Marks: ",total)
print("Percentage: ",percentage,"%")

if Phy >= 40 and Chem >= 40 and Maths >= 40:
  print("PASSED !!!")

else:
  print("FAILED !!!") 