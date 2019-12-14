from collections import Counter
f = open("python.txt","r")
print("Number of words in the file : \n")
print(Counter(f.read().split()))