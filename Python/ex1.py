name = input("Enter your name")
age = int(input("Enter your age"))

calc_age = 2020 + (100 - age)
print("Welcome " + name)
txt = "You will turn 100 years old in {}"

print(txt.format(calc_age))