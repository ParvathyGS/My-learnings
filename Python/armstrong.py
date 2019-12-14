sum = 0

num =int(input("enter number in 3 digits\n"))
temp = num
while (temp > 0):
	n1 = temp % 10
	sum = sum + (n1 ** 3)
	temp //= 10
if (num == sum):
	print("amstrong")
else:
	print("Not amstrong")


