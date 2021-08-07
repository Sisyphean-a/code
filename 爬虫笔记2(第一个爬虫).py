#爬取百度页面信息
import urllib.request
#from urllib import request   如果用这个的话，那么后面就可以用request代替urllib.request

import re #正则表达式的模块


#https比http安全性要高，如果用爬虫的话，https基本爬不进去
#所以我们一般都把这个转换一下，去掉s
url=r"http://www.baidu.com/"

#发送请求，获取响应信息,request自动创建请求对象，但是有些不便，所以可以
reponse=urllib.request.urlopen(url).read()
#这个是调用url请求中的打开，需要加上一个read(),不然没有办法读取，最后把这个赋值给一个变量
#所以就是调用这个模块的请求函数，打开要爬取的网址(这就是请求过程)，然后读取这个文件，使他展现(获取响应信息)

print(type(reponse))
#我们可以看到，它的类型是bytes,这就是二进制形式
#注意爬取信息是以二进制形式读取的，所以如果有汉字，会转换为二进制的形式，
#比如文件中的<title>百度一下，你就知道</title>
#就转换为title="\xe7\x99\xbe\xe5\xba\xa6\xe6\x90\x9c\xe7\xb4\xa2" />\n这是一种中间状态的二进制，也被称为字节码
#
#
print(len(reponse))

reponse=urllib.request.urlopen(url).read().decode()  #这个是解码，对应的是编码(encode)
#request自动创建请求对象，但是有些不便，所以可以创建自定义请求对象

#---------------------------------------------

#创建自定义请求对象
req=urllib.request.Request(url)  #这里只放了请求信息，我们还可以放入其他信息，去对抗网站上面的反爬机制
								 #换句话说，这句话就是对url的一个封装，就是说这个req还是url，只不过里面加入了一些信息
								 
reponse=urllib.request.urlopen(req).read().decode()

#---------------------------------------------

print(type(reponse))

pat=r"<title>(.*?)</title>"   #正则表达式进行数据清洗
data=re.findall(pat,reponse)  #在我们爬取出来的文件中查找所有符合正则表达式的字符(就是找到符合pat中格式的内容)
							  #因为信息会有多个，所以re.findall会将信息放到一个容器里边

print(type(data))             #说明这个正则表达式的类型是列表
							  #
print(data)					  

#因为我们只有一个数据，所以我们也可以直接输出它
print(data[0])	