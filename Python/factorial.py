n = int(input("enter the number"))
def cal_fact(n):
	if n == 1:
		return 1
	elif n > 1:
		return n * cal_fact(n-1)
print("the factorial is ")
print(cal_fact(n))