import requests
import re

def getHTMLText(url):
	try:
		header={
		 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
		 'referer': 'https://www.taobao.com/',
		  'cookie': 'cna=pbPkFzP7dVwCAXEFCEhq2MFY; lgc=tb781193753; tracknick=tb781193753; miid=67047681805637692; enc=9CTc59YyLm3xr0xn8TMDo9miA5Nn%2BuofC7ZQqKRqzbF1CkfF%2Fm3f%2FRHiAeEOO5d537f7kT58zaErRfiV04s7NJcLtxzqh6XPF2g7bxQz1Io%3D; thw=cn; UM_distinctid=17502f224ce225-00940b67d70f78-333376b-144000-17502f224cf2c5; hng=CN%7Czh-CN%7CCNY%7C156; '
		}
		r=requests.get(url,headers=header,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("读取失败")

		
def parsePage(ilt,html):
	try:
		plist=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlist=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plist)):
			price=eval(plist[i].split(':')[1])
			title=eval(tlist[i].split(':')[1])
			ilt.append([price,title])
		#print(ilt)
	except:
		print("提取失败")
	
def printGoodList(ilt):
	tplt="{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count=0
	for g in ilt:
		count=count+1
		print(tplt.format(count,g[0],g[1]))
	
if __name__ == '__main__':
	goods="书包"
	depth=2
	start_url='https://s.taobao.com/search?q='
	infoList=[]
	for i in range(depth):
		try:
			url=start_url+goods+"&s="+str(44*i)	
			html=getHTMLText(url)
			parsePage(infoList,html)
		except:
			continue
	printGoodList(infoList)
	input()
