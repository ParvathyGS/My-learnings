sum = 0

num =int(input("enter number in between 100 and 200\n"))

upper = 200
lower =  100
temp = num
while(temp > 0):
	n1 = temp % 10
	sum += n1 ** 3
	temp //= 10

if (num == sum):
	print("amstrong")
else:
	print("Not amstrong")
