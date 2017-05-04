import jieba
import numpy as np
from isIdealString import * 
import sys
import CrawlTitle
import time

WordsToIndex = np.load("WordsToIndex.npy").item()
BigramCounter = np.load("BigramCounter.npy").item()

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



pairs = SuspiciousList[20]
print(pairs)
question_word = ""

question_word += pairs[0]
question_word += pairs[1]
CrawlTitle.GetTitle(question_word)


