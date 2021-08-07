#自定义opener
#什么是opener，就是一种发送请求的对象
#
#我们之前使用的urlopen，它是一种特殊的opener（也就是模块帮我们构建好的）
#但是基本的urlopen()不包括代理，cookie等其他的HTTP/HTTPS高级功能，也就是说，它有很多限制。
#所以为了支持这些功能，我们通过request.build_opener()方法构建opener对象
#使用自定义的opener对象，调用open()方法发送请求
#
#
#那么什么是代理那？我们使用一台计算机，联网之后，IP地址是固定的
#我们不停地使用这个IP地址去访问一个网页，还是集中大量的访问，那么网站，很大可能把我们标记为爬虫
#这就仿佛前面的伪装浏览器一样，是同样的道理，只不过一个是IP，一个是用户代理
#解决方法也是差不多的，就是找其他的IP做代理，多个IP使用，就会更安全
#
#那么什么是cookle？我们在网页上留存的很多个人用户信息，都是有cookle保存的
#我们在后期也会加入cookle信息
#
#HTTP/HTTPS，两者都是网络协议，只不过HTTP是以明文的方式进行信息传输，HTTPS是以加密的方式进行信息传输
#HTTPS毫无疑问是更加安全的


#创建自定义opener
from urllib import request

#第一步，我们需要构建一个处理器对象（这个处理器不是硬件的处理器，是专门处理请求的对象）
http_hander=request.HTTPHandler()     #handler(处理器)，这个就是说请求函数里面的http处理器
									  #当然如果我们用的是HTTPS处理器的话，那么我们加一个s就行了

#第二步，创建一个自定义的opener
opener=request.build_opener(http_hander)     #这个就是创建(build)opener的函数了,需要一个变量去接收

#创建自定义请求对象
req=request.Request("http://www.baidu.com")

#发送请求，获取响应。这次发送请求就不使用urllib了，使用open
reponse=opener.open(req).read().decode()  #这个函数就很类似之前的urllib里面的request.urlopen方法
										  #注意这个里面的opener是第二步创建的opener，这个名字是可以改变的
										  #换句话说，这里面其实就是后面的open()是主要的，前面的只是一个变量

print(reponse)

