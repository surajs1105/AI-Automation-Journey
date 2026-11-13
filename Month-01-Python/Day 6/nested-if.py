age = int(input("Enter your Age: "))
has_id = input("Do you have an ID (yes/no): ")

if age >= 10:
  if has_id == "yes":
    print("Entry Allowed")
  else:
    print("Required ID")

else:
  print("Age Restriction: Entry Denied")