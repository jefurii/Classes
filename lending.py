import math

print("\t\t\t\t\t*****	  Amount Matrix\t*****")
print("\n\nAmount to Borrow\tMonthly Interest\tQuarterly Interest\tSemi-Annual Interest\t\Annual Interest")
A = input("\nEnter Amount: ")
M = input("Enter Months: ")
print("Choose Terms of Payment: ")
print("[1] MOnthly")
print("[2] Quarterly")
print("[3] Semi-Annual")
print("[4] Annual")
num = input("Enter Choice: ")
num = int(num)
if num == 1:
	print("Your Monthly Payment is: ")
if num == 2:
	print("Your Quarterly Payment is:")
if num == 3:
	print("Your Semi-Annual Payment is:")
if num == 4:
	print("Your Annual Payment is:")		