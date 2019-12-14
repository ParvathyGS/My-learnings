import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%U"))
print(x.strftime("%A"))
print(x.strftime("%j"))
print(x.strftime("%d"))
print(x.strftime("%w"))