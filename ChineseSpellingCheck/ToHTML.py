# -*- coding: utf-8 -*-
import mistune

def AddWrongWord(htmlpage, WrongWordList):
	InsertPosition = []
	for item in WrongWordList:
		WrongWords = ""
		WrongWords += item[0]
		WrongWords += item[1]

		Ins_start = htmlpage.find(WrongWords)

		if Ins_start == -1:
			print("Cannot find the Wrong Word" + item[0] + item[1])
			continue
		else:
			Ins_end = Ins_start + len(WrongWords)

		InsertPosition.append((Ins_start,Ins_end))

	NewPage = ""
	PreviousStart = 0
	for item in InsertPosition:
		NewPage += htmlpage[PreviousStart:item[0]]
		NewPage += "<mark>"
		NewPage += htmlpage[item[0]:item[1]]
		NewPage += "</mark>"
		PreviousStart = item[1]

	return NewPage


def ToHTML(file, OutputName, WrongWordList):

	markdown = mistune.Markdown()


	htmlpage = markdown(file)
	htmlpage = AddWrongWord(htmlpage,WrongWordList)

	try:
		OutputFile = open(OutputName,'r+')
	except FileNotFoundError:
		OutputFile = open(OutputName,'w')

	OutputFile.write("<head>\n")
	OutputFile.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>")
	OutputFile.write("</head>\n")

	OutputFile.write(htmlpage)

# ToHTML("./Test/test1.md","./Test/Testing.html", WrongWordList)

