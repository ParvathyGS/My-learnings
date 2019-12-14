fileHandle = open("python.txt","r")
lineList = fileHandle.readlines()
endpos = len(lineList)
startpos = endpos-10
for i in range(startpos,endpos):
	print(lineList[i])
