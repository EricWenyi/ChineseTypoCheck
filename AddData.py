# -*- coding: utf-8 -*-
import numpy as np
import jieba
import collections
from isIdealString import *



WordsToIndex = np.load("WordsToIndex.npy").item()
BigramCounter = np.load("BigramCounter.npy").item()


counter = len(WordsToIndex)

for i in range(1,):
	f = open("../SougouNews/File%d.txt" % i)

	file = f.read()
	seg_list = jieba.cut(file, cut_all = False)

	for word in seg_list:
		if word not in WordsToIndex:
			WordsToIndex[word] = counter
			counter = counter + 1

		if counter == len(WordsToIndex):
			PreviousWord = word
		else:
			if isIdealString(word,PreviousWord):
				BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] += 1
			PreviousWord = word

np.save('WordsToIndex.npy', WordsToIndex)
np.save('BigramCounter.npy', BigramCounter)
