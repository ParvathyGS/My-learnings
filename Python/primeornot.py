a = int(input("enter the number"))
for i in range(2,a):
	if (a % i == 0):
		print("Its not prime")
		break
	elif ( a <= 0):
		print("not prime")
		break
	else:
		print("prime")

	