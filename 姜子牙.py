import requests
import os

def getHTML(url,header,proxy):
	#try:
	r=requests.get(url,timeout=20,proxies=proxy)
	#r.raise_for_status()
	r.encoding=r.apparent_encoding
	return r.content
	#except :
	#	print("crawling fail")

def Download(html,path):
	try:
		if not os.path.exists(path):
			with open(path,"wb") as f:
				f.write(html)
				print(path+"crawling succeed!")	
	except :
		print(path+"Download fail")

if __name__ == '__main__':
	for x in range(1650):
		if x<10:
			url="https://youku.cdn7-okzy.com/20201117/21494_1a6a0739/1000k/hls/c29572e82eb00000"+str(x)+".ts"
			path="000"+str(x)+".ts"
		elif x<100:
			url="https://youku.cdn7-okzy.com/20201117/21494_1a6a0739/1000k/hls/c29572e82eb0000"+str(x)+".ts"
			path="00"+str(x)+".ts"
		elif x<1000:
			url="https://youku.cdn7-okzy.com/20201117/21494_1a6a0739/1000k/hls/c29572e82eb000"+str(x)+".ts"
			path="0"+str(x)+".ts"
		else:
			url="https://youku.cdn7-okzy.com/20201117/21494_1a6a0739/1000k/hls/c29572e82eb000"+str(x)+".ts"
			path=str(x)+".ts"
		
		header = {
   		 'Referer': 'https://www.91kanju.com/',
   		 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
			}

		proxy={'http':'http://175.43.32.35:9999/'}
		html=getHTML(url,header,proxy)
		Download(html,path)

