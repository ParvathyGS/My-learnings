n =int(input("enter limit of n"))
sum = 0
print("sum is \n")

while (n > 0):
	sum += n
	n = n - 1
print(sum)

'''
def sumofn(n):
	while(n > 0):
		sum = n + sumofn(n-1)
		print(sum)

sumofn(n)
'''