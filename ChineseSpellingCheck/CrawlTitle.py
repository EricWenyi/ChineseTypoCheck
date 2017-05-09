import sys 
import urllib
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request


def GetTitle(question_word):
	

	url = parse.quote('http://cn.bing.com/search?q='+question_word, safe='/:?=' )
	# print(url)

	req = request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    	}
	)

	htmlpage = request.urlopen(req).read().decode('utf8')
	# print(htmlpage)

	soup = BeautifulSoup(htmlpage,'html.parser')
	# print(soup)


	res = soup.find_all('strong')
	# print(res)

	NeedAutoCorrection = False

	if htmlpage.find('<div>是否只需要 <a') != -1:
		NeedAutoCorrection = True

	return res, NeedAutoCorrection



	#for item in res:
	#	print(item.get_text())
