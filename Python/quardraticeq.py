import math

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))

#x = −b ± √(b2 − 4ac) / 2a
res = math.sqrt((b * b) - (4 * a * c))

result1 = (-b + res) / (2 * a) 
result2 = (-b - res) / (2 * a) 

print("Result is ")
print(result1,result2)
