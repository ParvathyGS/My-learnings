f = open("demotxt.txt","a")
f.write("I am appending this line to file")
f.close()

f = open("demotxt.txt","r")
print(f.read())