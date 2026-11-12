age = int(input("Enter your age: "))
citizenship = input("Are you an Indian citizen? (yes/no): ")

if age >= 18 and citizenship.lower() == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")