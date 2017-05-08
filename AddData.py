# -*- coding: utf-8 -*-
import numpy as np
import jieba
import collections
from isIdealString import *



WordsToIndex = np.load("Test1_WordsToIndex.npy").item()
BigramCounter = np.load("Test1_BigramCounter_test.npy").item()


counter = len(WordsToIndex)

for i in range(1,1991):
	f = open("../SogouNews/Reduced/C000024/File%d.txt" % i)

	try:
		file = f.read()
	except UnicodeDecodeError:
		print("File error in File%d" % i)
		continue
	seg_list = jieba.cut(file, cut_all = False)
	PreviousWord = " "

	for word in seg_list:
		if word not in WordsToIndex:
			WordsToIndex[word] = counter
			counter = counter + 1

		if isIdealString(word,PreviousWord):
			BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] += 1
		PreviousWord = word

np.save('Test1_WordsToIndex.npy', WordsToIndex)
np.save('Test1_BigramCounter_test.npy', BigramCounter)
