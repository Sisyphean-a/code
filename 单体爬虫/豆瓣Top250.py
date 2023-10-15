import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

def getText(url,header):
	try:
		r=requests.get(url,headers=header)
		r.raise_for_status
		r.encoding=r.apparent_encoding
		return r.text
	except :
		print("爬取失败")
	

def bsText(html,ist):
	try:
		soup=BeautifulSoup(html,"html.parser")
		for child in soup.ol("li"):
			rank=child.find("em").string
			name=child.find("span").string
			dire=child.find("p").get_text().strip()
			num=child.find("span",class_="rating_num").string
			try:
				sum_up=child.find("span",class_="inq").string
			except :
				sum_up="获取评价失败"
			listt=("排名{:}\n影名:{:6}\n{:}\n评分:{:6}\n评价:{:6}\n".format(rank,name,dire,num,sum_up))
			ist.append(listt)
	except :
		print("编译失败")
		

def csvData(ist):
	


def down(path,ist):
	try:
		luo="----------------------------------------------------------------------------"
		with open(path,"w") as f:
			f.write("")
		for i in tqdm(ist):
			with open(path,"a",encoding="utf-8") as f:
				f.write(luo+"\n")
				f.write(i)
			time.sleep(0.01)
				#print("\r当前进度:{:2f}%".format(a*100/len(ist),end=""))
	except :
		print("写入失败")



if __name__ == '__main__':
	header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36', 'Referer': 'https://movie.douban.com/chart'}
	ist=[]
	path="豆瓣Top250.txt"
	for i in range(10):
		url="https://movie.douban.com/top250?start="+str(i*25)+"&filter="
		html=getText(url,header)
		bsText(html,ist)
	down(path,ist)
		
