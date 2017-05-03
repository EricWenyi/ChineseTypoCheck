import sys 
import urllib
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

question_word = "吃货 程序员" 

url = "http://www.baidu.com/s?wd=" + parse.quote(question_word) 



htmlpage = request.urlopen(url).read().decode("utf8")



"""
soup = BeautifulSoup(htmlpage,"html5lib") 
print(soup)



print(len(soup.findAll('div',{'class':'result c-container '})))

for result_table in soup.findAll('div',{'class':'result c-container '}):
    a_click = result_table.find("a") 
    print("------标题------\n" + a_click.renderContents()) #标题  
    print("------链接------\n" + str(a_click.get("href")))#链接  
    print("------描述------\n" + "result_table.find('div',{'class':'c-abstract'})")# 描述

"""