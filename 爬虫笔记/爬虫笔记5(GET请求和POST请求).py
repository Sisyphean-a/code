from urllib import request
import urllib

header={
	"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone \
	OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 \
	(KHTML, like Gecko) Version/7.0 Mobile/11B554a \
	Safari/9537.53"
}

#处理get请求

#处理get请求主要的是处理参数请求的问题
#如果传递的是英文，那么参数(wd)就是英文不变。如果是中文，那么就会转换格式,变成URL编码形式
#所以我们需要把参数变成这种格式才可以使用
#那么如何构造这个参数那？可以使用字典
wd={"wd":"北京"}

url="http://www.baidu.com/s?"

wdd=urllib.parse.urlencode(wd)

url=url+wdd

print(url)

req=request.Request(url)

repon=request.urlopen(req).read().decode()
#print(repon)


#处理post请求
#
#post请求不会放在URL里面。
#例如有道词典，就是放在form data(表单)中，
#有道翻译中国
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
formdata={"i": "中国",     #这个是请求
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
#这个需要先转码，转成UTF8的格式，然后可以赋值给data
data=urllib.parse.urlencode(formdata).encode(encoding="UTF8")
#如果Request()方法里面data参数有值，那么这个请求就是post请求
#如果没有，就是get请求
request=request.Request(url,data=data,headers=header)