n = int(input("enter no: of words"))

words = []

words = input("Enter words separated by comma ")
words_list  = words.split(",")
print("Printing all words\n")


unique = set(words_list)
print(len(unique))

for i in words_list:
	
# uniqueWords = [] 
# for i in words_list:
#       if not i in uniqueWords:
#           uniqueWords.append(i);

# print(len(uniqueWords))
# print("\n")

	if i in words_list:
		print(i)
