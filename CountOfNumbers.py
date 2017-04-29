# -*- coding: utf-8 -*-


import collections
import jieba

f = open("/home/eric9/Desktop/Linux_markdown/12.md")

# build dictionary
cnt = collections.Counter()

# read files 
file = f.read()

# sement words
seg_list = jieba.cut(file, cut_all=True)

# count numbiers
for word in seg_list:
	cnt[word] += 1

# get length of dictionary
length = len(cnt)

# get the order of the keys in a simple and easy way
#well....

# get the bigram 2-dimential array

my_list = [([0] * length) for i in range(length)]

