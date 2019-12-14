"""
inp_str = input("Enter string \n")
freq = {} 
for i in inp_str: 
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1  
# printing result  
print ("Count of all characters in " + inp_str + " is :\n " +  str(freq)) 
"""

# collections.Counter method 
from collections import Counter
inp_str = input("Enter string \n")
res = Counter(inp_str)
print("Count of all characters in " + inp_str + " is " + str(res))
