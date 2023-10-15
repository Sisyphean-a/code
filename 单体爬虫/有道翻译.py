import urllib
from urllib import request
import time
import re

#构建请求头文件
header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

#原本的URL是不可用的，需要去掉一个_o才可以
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"


key=input("请输入：")
#key="你好"

#post请求，需要传递的参数
formdata={"i": key,     #这个是请求
		  "from": "AUTO",  #从什么语言开始，这里设置为自动
		  "to": "AUTO",    #从什么语言结束，这里设置为自动
		  "smartresult": "dict",
		  "client": "fanyideskweb",
		  "salt": "15770066934286",
		  "sign": "4eaede0ff963cdd843f6a99b2d9b8a07",
		  "ts": "1577006693428",
		  "bv": "40cd57288129392e94ffd3426bd5537c",
		  "doctype": "json",
	 	  "version": "2.1",
		  "keyfrom": "fanyi.web",
		  "action": "FY_BY_REALTlME"}

data=urllib.parse.urlencode(formdata).encode(encoding="utf-8")

req=request.Request(url,data=data,headers=header)

resp=request.urlopen(req).read().decode()

#---------
ree=r'"tgt":"(.*?)"}]]}'

data=re.findall(ree,resp)
#---------
#{"type":"ZH_CN2EN","errorCode":0,"elapsedTime":2,"translateResult":[[{"src":"你好","tgt":"hello"}]]}

print(data[0])

time.sleep(10)