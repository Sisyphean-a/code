import requests
from lxml import etree
import csv

def getHTML(url,header):
	r=requests.get(url,headers=header,timeout=20)
	r.encoding='utf-8'
	return r.text

def cssHTML(html,dic,url_num):
	html=etree.HTML(html)
	path_num='//*[@id='+url_num+']/div'
	lis=html.xpath(path_num)
	for x in range(len(lis)):
		path=path_num+'['+str(x+1)+']/a/text()'
		title_name=html.xpath(path)

		path_id=html.xpath(path_num+'['+str(x+1)+']/@id')
		title_lis=html.xpath('//*[@id="'+path_id[0]+'"]/div')
		ist=[]
		for i in range(len(title_lis)):
			title_child_name=html.xpath('//*[@id="'+path_id[0]+'"]/div['+str(i+1)+']/a/text()')
			ist.append(title_child_name[0])
		dic[title_name[0]]=ist
	#print(dic)

def csvList(path,dic):
	with open(path,'w',newline='',encoding='utf-8') as f:
		csv_row=csv.writer(f)
		#csv_row.writerow(dic.keys())
		for row in dic.keys():
			csv_row.writerow([row])
			csv_row.writerow(dic[row])


if __name__ == '__main__':
	dic={}
	path='plan.csv'
	header={
		'Connection': 'keep-alive',
	    'Cache-Control': 'max-age=0',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Referer': 'https://www.liaoxuefeng.com/wiki/1022910821149312/1023020895584256',
	    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
	}
	url="https://www.liaoxuefeng.com/wiki/1016959663602400"
	url_num=url.split("/")[-1]
	html=getHTML(url,header)
	cssHTML(html,dic,url_num)
	csvList(path,dic)
