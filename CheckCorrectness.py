import sys


def CheckCorrectness(res, question_word):

	counter = 0

	for highlightWords in res:
		content = highlightWords.get_text()
		
		if content.find(question_word) != -1:
			counter += 1

	if counter > 4:
		return True
	else:
		return False