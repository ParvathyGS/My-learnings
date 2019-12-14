a = [[1,2,3],
 	 [4,5,6],
 	 [7,8,9]]
b =  [[1,2,3],
 	 [4,5,6],
 	 [7,8,9]]
a1 = len(a)
b1 = len(b[0])
sum =[[0,0,0],
 	 [0,0,0],
 	 [0,0,0]]
#print(a1,b1)
for i in range(a1):
	for j in range(b1):
		sum[i][j] = a[i][j] + b[i][j]
for r in sum:
	print(r)
