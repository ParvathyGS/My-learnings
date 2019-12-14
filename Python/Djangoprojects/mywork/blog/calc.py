def calc(n):
	if n == 1:
		return 1
	else:
		return (n * calc(n-1))

# n = 5
# print("Factorial of 5 is ",calc(n))
num = 4
print(calc(num))	