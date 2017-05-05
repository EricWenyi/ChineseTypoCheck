# -*- coding: utf-8 -*-
import collections
import jieba
import numpy as np
from isIdealString import * 




# calcualte the frequency of each word 
# WordFrequency = collections.Counter()

WordsToIndex = collections.defaultdict(int)

counter = 0
BigramCounter = collections.defaultdict(int)



for i in range(1,750):

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
				BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] += 1
			PreviousWord = word

		# initialize WordFrequency
		# WordFrequency[word] += 1

np.save('WordsToIndex.npy', WordsToIndex)
np.save('BigramCounter.npy', BigramCounter)

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



















