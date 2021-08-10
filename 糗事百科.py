import requests
from bs4 import BeautifulSoup


def getHTTPText(url,header,proxy):
    try:
        r=requests.get(url,headers=header,timeout=5,proxies=proxy)
        r.raise_for_status()
        return r.text
    except :
        print("爬取失败")


def bs_text(listt,html):
    soup=BeautifulSoup(html,"html.parser")
    listt=soup.find_all("div",class_="article")

    for x in range(len(listt)):
        name=listt[x].find("h2").string
        age=listt[x].find("div",class_="articleGender").string
        text=listt[x].find("div",class_="content").find("span").get_text()
        funny=listt[x].find("span","stats-vote").find("i").string
        txt=("昵称:{:8}年龄:{:4}\t点赞:{:5}\n{:}".format(name,age,funny,text))

        save_text("xiushi.txt",txt)


def save_text(path,*args):
    lun="---------------------------------------"
    for i in args:
        with open(path,"a",encoding="UTF-8") as f:
            f.write(lun+"\n")
            f.write(i)


if __name__ == '__main__':
    listt=[]
    for i in range(10):
        url="https://www.qiushibaike.com/text/page/{}".format(i)
        proxy={"IP":"117.64.224.33"}
        header={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
        html=getHTTPText(url,header,proxy)
        bs_text(listt,html)

