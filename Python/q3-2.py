n = int(input("enter no of lines to read\n"))
if n <= 0:
	print("file empty")
elif n > 0:
	f = open("python.txt","r")
	for x in range(0,n):
		print(f.readline())
	
