class myNumb:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a < 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration
myObj = myNumb()
myiter = iter(myObj)
for x in myiter:
	print(x)
'''
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''