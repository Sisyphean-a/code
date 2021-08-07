import requests

#使用requests发送请求，使用的是其中的get函数
req=requests.get("http://www.biadu.com")

print(req)

#输出结果是<Response [200]>,200的意思是正常，意思是请求结果是正常的
#如果想要输出结果，我们可以在请求后面加一个.text来转换

req=requests.get("http://www.biadu.com").text
#但是这样输出的结果是以字符串的形式响应，这样有乱码，
#所以我们可以换用.content,这会以二进制的结果输出，然后可以再用一个decode()显化汉字

req=requests.get("http://www.biadu.com").content.decode()

#print(req)

#除了get请求之外，我们还可以使用request函数（是的，这个模块里面也有，只是有点不同），在参数第一位上面加一个"get"就可以了
req=requests.request("get","http://www.biadu.com")
#结果是一样的，嗯，好像没什么用啊。

print(req)
