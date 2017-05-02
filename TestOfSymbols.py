# -*- coding: utf-8 -*-


import jieba

stop_symbols = [".", ",","。","#", "\n", "(", "、", "`", "，", 
"##","$","###","####", "-", "+","|","/", ":", "：","*","?","!","@","#"," ","\'","\"","\\"]

f = open("./Data/File1.md")

file = f.read()

seg_list = jieba.cut(file, cut_all=False)

for word in seg_list:
	if word in stop_symbols:
		continue;
	else:
		print(word,end='/')
