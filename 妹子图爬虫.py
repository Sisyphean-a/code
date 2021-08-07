import requests
import os

def function():
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(path):
			r=requests.get(url,headers=kv,timeout=3)
			with open(path,'wb') as f:
				f.write(r.content)
				print("爬取成功")
		else:
			print("此文件已存在")
	except:
		print("爬取失败")

def urll(url0,i):
	urlNumber=url0.split('/')
	urlFront=url0[0:35]
	urlOne=urlNumber[-1][3:5]
	if i<10:
		nub="0"+str(i)
	elif i>=10:
		nub=str(i)
	url_new=urlFront+nub+'.jpg'
	return url_new

if __name__ == '__main__':
	url0=input('url=:')
	numb=int(input("页数："))
	for i in range(1,numb):
		url=urll(url0,i)
		kv={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36","Referer":"https://www.mzitu.com/"}
		root="E://00//"+url.split('/')[-3]+url.split('/')[-2]+"//"
		path=root+url.split('/')[-1]
		print(path)
		function()
		i=i+1

