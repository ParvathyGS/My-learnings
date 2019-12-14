thisList = ["apple","banana","guava"]
f = open("newfile.txt","w")
for x in thisList:
	f.write("\n" + x)
f.close()
f = open("newfile.txt","r")
print(f.read())