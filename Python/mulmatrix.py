X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

res = [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]
for i in range(len(X)):
	for j in range(len(Y[0])):
		for k in range(len(Y)):
			res[i][j] = X[i][k] * Y[k][j]
for r in res:
	print(r)