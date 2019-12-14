class Person:
	def __init__(self,fname,lname):
		self.fname = fname
		self.lname = lname
	def myFunc(self):
		print(self.fname,self.lname)
class Student(Person):
	def __init__(self,fname,lname,age):
		super().__init__(fname,lname)
		self.age = age
	def printName(self):
	    print(self.fname,self.lname,self.age)
			
#p1 = Person("John","Duo")
s1 = Student("Riya","diva",45)
s1.printName()
