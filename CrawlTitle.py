import sys 
import urllib
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request


def GetTitle(question_word):
	

	url = "http://www.baidu.com/s?wd=" + parse.quote(question_word) 
	# print(url)

	req = request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	}
	)

	htmlpage = request.urlopen(req).read().decode("utf8")
	print(htmlpage)

	soup = BeautifulSoup(htmlpage,'html.parser') 
	# print(soup)


	res = soup.find_all('em')
	print(res)


GetTitle("python基本使用")

"""
print(len(soup.findAll('div',{'class':'result c-container '})))

for result_table in soup.findAll('div',{'class':'result c-container '}):
    a_click = result_table.find("a") 
    print("------标题------\n" + a_click.renderContents()) #标题  
    print("------链接------\n" + str(a_click.get("href")))#链接  
    print("------描述------\n" + "result_table.find('div',{'class':'c-abstract'})")# 描述

"""