# -*- coding: utf-8 -*-


import collections
import jieba


f = open("./Data/File1.md")

# build dictionary
WordFrequency = collections.Counter()

# read files 
file = f.read()

# sement words
seg_list = jieba.cut(file, cut_all=False)

# count numbers 
# cnt is the 1d counter
# WordsToIndex is a words-->index dictionary

WordsToIndex = collections.defaultdict(int)
counter = 0
BigramCounter = collections.defaultdict(int)

for word in seg_list:
	# initalize my WordsToIndex
	if word not in WordsToIndex:
		WordsToIndex[word] = counter
		counter = counter + 1

	# initialize BigramCounter
	if counter == 1:
		PreviousWord = word
	else:
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
IndexToWords = []

for item in WordsToIndex:
	IndexToWords.append(item)












