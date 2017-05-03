# -*- coding: utf-8 -*-
import collections
import jieba

stop_symbols = [".", ",","。","#", "\n", "(", "、", "`", "，", \
"##","$","###","####", "-", "+","|","/", ":", "：","*","?","!","@", \
"#"," ","\'","\"","\\",";","%",")","(","<",">","？","！","；","「","」","（","）" \
"[","]","{","}","“","”","）","《","》"]


def isIdealString(word, PreviousWord):
	if PreviousWord not in stop_symbols \
	and word not in stop_symbols \
	and not word.encode("UTF-8").isalpha() \
	and not PreviousWord.encode("UTF-8").isalpha():
		return True
	else:
		return False

# calcualte the frequency of each word 
WordFrequency = collections.Counter()

WordsToIndex = collections.defaultdict(int)

counter = 0
BigramCounter = collections.defaultdict(int)



for i in range(2,3):

	f = open("../freecourse/File%d.md" % i)


	# read files 
	file = f.read()

	# sement words
	seg_list = jieba.cut(file, cut_all=False)

	# count numbers 
	# cnt is the 1d counter
	# WordsToIndex is a words-->index dictionary



	for word in seg_list:
		# initalize my WordsToIndex
		if word not in WordsToIndex:
			WordsToIndex[word] = counter
			counter = counter + 1

		# initialize BigramCounter
		if counter == 1:
			PreviousWord = word
		else:
			if isIdealString(word,PreviousWord): 
				print(word)
				BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] += 1
			PreviousWord = word

		# initialize cnt
		WordFrequency[word] += 1

"""
for item in BigramCounter:
	print(str(item) + str(BigramCounter[item]))


for item in WordsToIndex:
	if WordsToIndex[item] == 37:
		print("37:" + item)
	if WordsToIndex[item] == 38:
		print("38:" + item)

"""

# start another mapping from index to words
# This is an array however

"""
IndexToWords = []

for item in WordsToIndex:
	IndexToWords.append(item)
"""


# handling with user input 


f = open("./Test/test.md")

file = f.read()

seg_list = jieba.cut(file,cut_all=False)

SuspiciousList = []


counter = False

for word in seg_list:
	if counter == False:
		PreviousWord = word
		counter = True
	else:
		if isIdealString(word,PreviousWord):
			if BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] == 0:
				SuspiciousList.append((PreviousWord,word))
		PreviousWord = word




















