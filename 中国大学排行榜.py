import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		a=r.text
		return a
	except:
		return "shibai"

def findHTMLText(ulist,html):
	soup=BeautifulSoup(html,"html.parser")
	for chil in soup.find('tbody').children:
		if isinstance(chil,bs4.element.Tag):
			tds=chil('td')
			tda=chil('a')
		ulist.append([tds[0].string,tda[0].string,tds[4].string])
		


def printText(ulist,num):
	print("{:^10}{:^10}{:^10}".format("排名","学校","评分"))
	for i in range(num):
		u=ulist[i]
		print("{:^10}{:^10}{:^10}".format(u[0],u[1],u[2]))

if __name__ == '__main__':
	ulist = []
	url='https://www.shanghairanking.cn/rankings/bcur/2020'
	html=getHTMLText(url)
	findHTMLText(ulist,html)
	printText(ulist,20)
	input("")
