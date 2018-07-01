# put your code here.
#open file
word_list = []
poem = open("test.txt")
for line in poem:
	# print(line.rstrip('\n'))
	line = line.rstrip('\n').split(' ')
	for word in line:
		if word[-1] == "?" or ",":
			word = word[0:-1]

	# sentence = line.split(' ')
	#print(sentence)
	#word_list = word_list + sentence #adds the lists into one list
	word_list.extend(line)

master_list = []
# for word in word_list:
# 	lower_word = word.lower()
# 	master_list.append(lower_word)

master_list = [word.lower() for word in word_list]

print(master_list)



def get_letter_counts(lst):
#create a dictionary
# key = word
# value = count
	word_count = {}
# go through our word list and add it to the dictionary:
	for word in lst:
		# if word is not in dictionary, add it with a count of 0
		if word not in word_count:
			word_count[word] = 1
		else:
			word_count[word] += 1

	print(word_count)

get_letter_counts(master_list)
# if word is in dictionary, increase count by 1



#



# word_list = []
# #make a list of the words
# for line in poem:
# 	line = line.rsplit()
# 	word_list.append(poem.split(' '))
# print(word_list)

# def wordcount(filename):

# 	word_counts = {}



	#count words

	#return a dictionary