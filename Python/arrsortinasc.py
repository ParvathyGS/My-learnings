arr = [12,34,67,87,34,67,45,22,1,90,21,65,86]
sortarr = []
for i in range(0,len(arr)):
	for j in range(i+1,len(arr)):
		if arr[i] > arr[j]:
			temp = arr[i]
			arr[i] =arr[j]
			arr[j] = temp
for i in range(0,len(arr)):
	print(arr[i])