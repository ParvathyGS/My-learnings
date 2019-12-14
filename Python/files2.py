f = open("demofile.txt","a")
f.write("My first file pgm!!")
f.close()

f = open("demofile.txt","r")
print(f.read())