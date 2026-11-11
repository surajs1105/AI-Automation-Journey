balance = 50000

withdrawal = float(input("Enter the amount to withdrawal: "))

if withdrawal > 0 and withdrawal <= balance:
  balance -= withdrawal
  print("Withdrawal Successful !")
  print("Available Balance: ",balance)
else:
  print("Insufficient Balance !")