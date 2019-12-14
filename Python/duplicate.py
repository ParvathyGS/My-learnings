array1 = ["apple","cherry","grapes","orange","guava","apple","cherry","olive"]

for i in range(0,len(array1)):
	for j in range(i+1,len(array1)):
		if array1[i] == array1[j]:
			print(array1[i])