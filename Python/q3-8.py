f = open("python.txt","r")
wordList = f.read().split()
longest_word = ''
for word in wordList:
	if len(word) > len(longest_word):
		longest_word = word
print("The longest word is " + longest_word)
