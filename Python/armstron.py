n = int(input("Enter the number"))
sum = 0
temp = n
while(temp > 0):
	digit = temp%10
	sum = sum + digit ** 3
	temp = temp / 10
if (sum == n):
	print("amstrong")
else:
	print("not amstrong")

