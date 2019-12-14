n = int(input("Enter the number"))
print("the factorial is")
def fact1(n):
	if (n==0 or n==1):
		return 1
		return n * fact1(n-1)
print(fact1(n))
#print("The factorial of {} is".format(num))
