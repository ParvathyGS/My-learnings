a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
print("greatest number is ")
if (a > b) & (a > c):
	print(a)
elif (b > a) & (b > c):
	print(b)
else:
	print(c)