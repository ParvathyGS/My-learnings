n = int(input("Enter the limit"))
# for row in range(1,n):
# 	for column in range(1,row+1):
# 		print(column,end=" ")
# 	print('\n')


for row in range(n+1):
	for column in range(row):
		print(row, end=' ')
	print("\n")

