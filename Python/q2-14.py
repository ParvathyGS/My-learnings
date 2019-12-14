thisSet = {'apple','banana','mango','kiwi'}
print(thisSet)
x = input("Enter the element to be removed \n")
if x in thisSet:
	thisSet.remove(x)
print(thisSet)