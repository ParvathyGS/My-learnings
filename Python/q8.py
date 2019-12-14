import random
print("Guess a number between 0 and 10")
num = int(input())
print(num)
randnum = int(random.randrange(0,10))
txt = "The guessed number is {}"
print(txt.format(num))
txt1 = "The random number generated is {}"
print(txt1.format(randnum))
if num < randnum:
	print("You guessed too low!!")
elif num > randnum:
	print("You guessed too high!!")
else:
	print("Congrats! You guessed the correct number!!")

