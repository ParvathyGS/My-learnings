class myClass:
	def __init__(self,fname,lname):
		self.fname = fname
		self.lname = lname
		#print(fname + " " + lname)
	
	def muFunc(self):
		print("name is " + self.fname + " " + self.lname)

p1 = myClass("Parvathy","Arun")
p1.lname = "Suresh"
p1.muFunc()