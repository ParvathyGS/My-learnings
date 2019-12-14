class Person:
	def __init__(self,fname,lname):
		self.fname = fname
		self.lname = lname
	def myFunc(self):
		print("name is " + self.fname + " " + self.lname)
class  Student(Person):
	def __init__(self,fname,lname,age):
		self.fname = fname
		self.lname = lname
		self.age = age
	def func(self):
		print("I am " + str(self.age) + " old")
	"""docstring for  Student
"Persf __init__(self, arg):
		super( Student
		,Person.__init__()
		self.arg = arg
"""		
p1 = Person("Parvathy","Arun")
p2 = Student("Arun","Babu",34)
p1.myFunc()
p2.myFunc()
p2.func()	
