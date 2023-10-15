#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import re
from tqdm import tqdm

def getHTML(url,header):
	r=requests.get(url)#,headers=header)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	return r.text

def xmlData(html,ist):
	html=etree.HTML(html)
	title=html.xpath('//*[contains(@id,"normalthread_13")]/tr/th/a[2]/text()')
	name=html.xpath('//*[contains(@id,"normalthread_13")]/tr/td[2]/cite/a/text()')
	brow_num=html.xpath('//*[contains(@id,"normalthread_13")]/tr/td[3]/em/text()')
	urll=html.xpath('//*[contains(@id,"normalthread_13")]/tr/th/a[2]/@href')
	for x in range(44):
		ist.append({'标题':title[x],'作者':name[x],'浏览量':brow_num[x],'url':urll[x]})

def newHTML(ist,urll,header):
	for x in range(len(ist)):
		try:
			url='https://www.52pojie.cn/'+ist[x]['url']
			html=getHTML(url,header)
			ree=re.findall(r'(^https|http.*)',html)
			urll.append({'inter_url':ree})
			print(ist[x]['标题']+'获取结束')
		except:
			print('url失效')

def DownData(ist,path,urll):
	for x in range(len(ist)):
		with open(path,'a',encoding='utf-8') as f:
			f.write("标题："+ist[x]['标题']+'\n')
			f.write("作者："+ist[x]['作者']+'\n')
			f.write("浏览量："+ist[x]['浏览量']+'\n')
			f.write("链接："+'https://www.52pojie.cn/'+ist[x]['url']+'\n')
			f.write("网盘链接:"+urll[x]['inter_url']+'\n\n')


if __name__ == '__main__':
	header={}
	ist=[]	
	urll=[]
	path='52pojie.txt'
	for x in tqdm(range(1)):
		url="https://www.52pojie.cn/forum-16-"+str(x+1)+".html"
		html=getHTML(url,header)
		xmlData(html,ist)

	newHTML(ist,urll,header)
	DownData(ist,path,urll)


