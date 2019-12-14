import os

f = open("demofile.txt","w")
f.write("My first file pgm!!")
f.close()

# f = open("demofile.txt","r")
# print(f.read())

# f = open("demo.txt","w")
# f.write("Helloo.....")
# f.close()

# f = open("demo.txt","r")
# print(f.read())

# f = open("myfile1.txt", "r")
if os.path.exists("demo.txt"):
	os.remove("demo.txt")
else:
	print("File does not exist")

os.rmdir("New Folder")