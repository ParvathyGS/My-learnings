import random 
def convert(pswd):
	password = ""
	for x in pswd:
		password += x
	return password
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',0,1,2,3,4,5,6,7,8,9,'_','#','*','!','@','$','&','?','/','.']
inp = int(input("Please enter the length of new password to be created...\n"))
pswd = random.choices(alpha,k = inp)
print(convert(pswd))
