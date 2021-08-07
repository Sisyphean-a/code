import csv
import requests
from lxml import etree
import json

def getHTML(url,header):
	r=requests.get(url,headers=header)
	r.raise_for_status
	r.encoding='utf-8'
	return r.text

def xpathHTML(html,ist):
	data=json.loads(html)
	#print(data)
	for x in range(200):
		name=data['subjects'][x]['title']
		score=data['subjects'][x]['rate']
		html_url=data['subjects'][x]['url']
		picture_url=data['subjects'][x]['cover']
		ist.append({"name":name,"score":score,"html_url":html_url,"picture_url":picture_url})

def csvHTML(path,ist):
	with open(path,'w',newline='',encoding='utf-8') as f:
		csv_w=csv.writer(f)
		csv_w.writerow(['评分','	影名','地址','图片地址'])
		for data in ist:
			csv_w.writerow([data["score"],data["name"],data["html_url"],data["picture_url"]])

if __name__ == '__main__':
	url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'
	header={
	    'Connection': 'keep-alive',
	    'Accept': '*/*',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
	    'X-Requested-With': 'XMLHttpRequest',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	    'Referer': 'https://movie.douban.com/explore',
	    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
	}
	ist=[]
	path='豆瓣电影.csv'
	html=getHTML(url,header)
	print('获取html成功')
	xpathHTML(html,ist)
	print('信息处理完成')
	csvHTML(path,ist)
	print('信息保存成功')
	print(ist[1])




'''
def csvdata():
	with open('new1.csv','a',encoding='utf-8') as f:
		csv_w=csv.writer(f)
		csv_w.writerow([44,55,66])
		csv_w.writerow([2,5,7])

	with open('new.csv','r',encoding='utf-8') as f:
		csv_r=csv.DictReader(f)
		for x in csv_r:
			print(x)
'''

