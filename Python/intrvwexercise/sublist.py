#Python program to print all  
# sublist from a given list  
# function to generate all the sub lists 
def displaysublist(A): 
   # store all the sublists  
   B = [[ ]] 
      
   # first loop  
   for i in range(len(A) + 1):
      # second loop  
      for j in range(i + 1, len(A) + 1):   
         print(i,j)      
         # slice the subarray  
         sub = A[i:j] 
         B.append(sub) 
   return B 
  
# driver code 
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print("SUBLIST IS ::>",displaysublist(A)) 