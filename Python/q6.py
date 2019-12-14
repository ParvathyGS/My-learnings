print("Enter a string to be checked for palindrome or not")
str = input()
revstr = ""
for x in str:
	revstr = x + revstr
if str == revstr:
	print("The string " + str + " is palindrome!!")
else:
	print("The string " + str + " is not palindrome!!")
