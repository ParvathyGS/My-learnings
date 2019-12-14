# list1 = int(input("Enter the numbers seperated by space \n"))

# # creating sum_list function 
# def sumOfList(list, size): 
#    if (size == 0): 
#      return 0
#    else: 
#      return list[size - 1] + sumOfList(list, size - 1) 
# # Driver code      
# total = sumOfList(list1,len(list1))

# print("Sum of all elements in given list: ", total) 
# list = []
# n = int(input("Enter the no:of elements"))
# for x in range(0,n):
# 	ele = int(input)
# list.append(ele)
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((list)))
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 

print("enter a list")
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("The sum is ")
print(sum(lst))