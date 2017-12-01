import math
import random

#A = input("\n\n\n\nEnter Amount: ")
#M = input("Enter Months: ")
rand = (1000)
tri = True
while tri:
	A = input("\n\n\n\nEnter Amount: ")
	A = int(A)
	Monthlya = A *.05 
	Monthlyb = A * .6
	Monthlyc = A * .7
	Monthlyd = A * .16
	Monthlye = A * .17
	Monthlyf = A * .18
	Monthlyg = A * .19
	Monthlyh = A * .20
	Monthlyi = A * .21
	Monthlyj = A * .27
	Monthlyk = A * .29
	Monthlyl = A * .30
	if A < 1001:
		print("Payable in 1 month:	",Monthlya,) #Months
		break
	if A > 1000000:
		print("Invalid")	
		break
	if A > 1000 and A <10001:
		MP = input("How Many Months to Pay?	")
		MP = int(MP)
		print("[1] Monthly")
		print("[2] Quarterly")
		# A = input("Choose Terms of Payment: ")
		# print("[1] Monthly")
		# print("[2] Quarterly")
		EC = input("\nEnter Choice: ") # Months % Quarterly
		EC = int(EC)
		if EC == 1:
		 	print("\n\n\n\nMonthly Payment: ",(Monthlya+A)/MP,) 
		 	break
		if EC == 2:
		 	print("\n\n\n\nQuarterly Payment: ",(Monthlyd+A)/MP/4,)
		 	break
	if A > 10001 and A <50001:	 
		MP = input("How Many Months to Pay?	")
		MP = int(MP)
		print("[1] Monthly")
		print("[2] Quarterly")
		print("[3] Semi-Annual")
		EC = input("\nEnter Choice: ")
		EC = int(EC)
		if EC == 1:
		 	print("\n\n\n\nMonthly Payment: ",(Monthlya+A)/MP,)
		 	break
		if EC == 2:
		 	print("\n\n\n\nQuarterly Payment: ",(Monthlyd+A)/MP/4,)
		 	break
		if EC == 3:
		 	print("\n\n\n\nSemi-Annual Payment: ",(Monthlyg+A)/MP/2*MP,)
		 	break	
	if A > 50000 and A <100001:	 
		MP = input("How Many Months to Pay?	")
		MP = int(MP)
		print("[1] Monthly")
		print("[2] Quarterly")
		print("[3] Semi-Annual")
		print("[4] Annual")	
		EC = input("\nEnter Choice: ")
		EC = int(EC)
		if EC == 1:
		 	print("\n\n\n\nMonthly Payment: ",(Monthlyb+A)/MP,)
		 	break
		if EC == 2:
		 	print("\n\n\n\nQuarterly Payment: ",(Monthlye+A)/MP/4*MP,)
		 	break
		if EC == 3:
		 	print("\n\n\n\nMonthly Payment: ",(Monthlyg+A)/MP/2,)
		 	break
		if EC == 4:
		 	print("\n\n\n\nQuarterly Payment: ",(Monthlyj+A)/MP,)
		 	break		 	