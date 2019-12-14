"""

n = int(input("Enter the value of n...\n"))
sum = []
def sum_list(n):
	return n + sum_list(n-2)
print("sum is ")	
sum_list(n)

"""
n = int(input("Enter the value of n...\n"))
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
print("the sum is ")
print(sum_series(n))

