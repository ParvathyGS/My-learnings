print("Enter a natural number to find its divisors")
num = int(input())
print("The divisors are ")
for x in range(1,num):
	if num % x == 0:	
		print(x)
