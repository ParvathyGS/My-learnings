numlist = [12,10,35,31,9,55,79,30,60,5,3,85]
print(numlist)
y = list(filter(lambda x : (x % 5 == 0), numlist))

print(y)