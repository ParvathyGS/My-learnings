n = int(input("Enter the limit"))

for row in range(n+1):
	for column in range(n+1):
		print(column * '* ')
	print("\n")
	break
