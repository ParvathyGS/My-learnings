print("1.Addition\n")
print("2.Substraction\n")
print("3.Multiplication\n")
print("4.Division\n")
opr = int(input("Enter the serial number of operation to perform"))
num1 =int(input("Enter the first number"))
num2 =int(input("Enter the second number"))
add,sub,mul,div = 0,0,0,0
if (opr == 1):
	add = num1 + num2
	print("Sum is ",add)
elif(opr == 2):
	sub = num1 - num2
	print("Difference is ",sub)
elif(opr == 3):
	mul = num1 * num2
	print("Product is ",mul)
elif(opr == 4):
	div = num1 / num2
	print("Divided value is ",div)



