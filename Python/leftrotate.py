array1 = ["apple","cherry","grapes","orange","guava","olive"]
first = array1[0]
length = int(len(array1))
for i in range(0,len(array1)-1):
	array1[i] = array1[i+1]

array1[length-1] = first

for i in range(1):
	print(array1)
