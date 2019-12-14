num = int(input("Enter the number"))
n = num
c = 0
digitval = 0
while (n > 0):
	n = n % 10

	digitval = digitval + (digit * digit * digit)
	n = n // 10
if num == digitval:
	print("amstrong")
else:
	print("Not amstrong")

