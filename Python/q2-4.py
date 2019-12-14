from collections import Counter 
inp_str = input("Enter the string\n")
res = Counter(inp_str)
print("The repeated charecters are ")
for x,y in res.items():
	if res[x] > 1:
		print(x,str(y))
