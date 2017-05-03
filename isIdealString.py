def isIdealString(word, PreviousWord):
	if PreviousWord not in stop_symbols \
	and word not in stop_symbols \
	and not word.encode("UTF-8").isalpha() \
	and not PreviousWord.encode("UTF-8").isalpha() \
	and not word.isdigit() \
	and not PreviousWord.isdigit():
		return True
	else:
		return False

stop_symbols = [".", ",","。","#", "\n", "(", "、", "`", "，", \
"##","$","###","####", "-", "+","|","/", ":", "：","*","?","!","@", \
"#"," ","\'","\"","\\",";","%",")","(","<",">","？","！","；","「","」","（","）" \
"[","]","{","}","“","”","）","《","》","=","\t","】"]