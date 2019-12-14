print("Enter your name")
name = input()
print("Enter your Age")
age = input()
print("Welcome " + name)
x = 100 - int(age)
y = 2019 + x
txt = "Hey! You will turn 100 years old in {}"
print(txt.format(y))