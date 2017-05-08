import jieba
import numpy as np
from isIdealString import * 
import sys
import CrawlTitle
import time
from CheckCorrectness import CheckCorrectness

WordsToIndex = np.load("Test1_WordsToIndex.npy").item()
BigramCounter = np.load("Test1_BigramCounter_test.npy").item()

f = open("./Test/test.md")

file = f.read()

seg_list = jieba.cut(file,cut_all=False)

SuspiciousList = []


counter = False


# get the word in the test doc 
for word in seg_list:
	if counter == False:
		PreviousWord = word
		counter = True
	else:
		if isIdealString(word,PreviousWord): 
			if BigramCounter[WordsToIndex[PreviousWord],WordsToIndex[word]] == 0:
				SuspiciousList.append((PreviousWord,word))
		PreviousWord = word

print(SuspiciousList)

time.sleep(5)


# get the worong word according to the result of search


WrongWordList = []

for pairs in SuspiciousList:
	question_word = ""
	question_word += pairs[0]
	question_word += pairs[1]
	res, NeedAutoCorrection = CrawlTitle.GetTitle(question_word)
	print(res)
	if not CheckCorrectness(res, question_word) or NeedAutoCorrection:
		WrongWordList.append(pairs)
	time.sleep(0.5)

print(WrongWordList)
print(len(WrongWordList))


