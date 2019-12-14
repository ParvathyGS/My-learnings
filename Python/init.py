class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def myFunc(self):
		print("Hello.. My name is " + self.name)
		#print("I am " + str(self.age) + " years old!!")
p1 = Person("John",35)

del p1.age
p1.myFunc()
del p1
print(p1)

#print(p1.name)
#print(p1.age)