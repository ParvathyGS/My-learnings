n = int(input("enter the number"))
def sumofn(n):
	if n == 1:
		return 1
	elif n > 1:
		return n + sumofn(n-1)
print("sum is ")
print(sumofn(n))