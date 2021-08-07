#爬虫并不受欢迎，所以很多网站都会设立反爬虫机制。
#
#反爬虫机制
#反爬虫机制1：最常用的反爬虫机制，判断用户是否是浏览器访问，即，判断浏览器名称
#			   我们的爬虫，是通过模块(这里我们用的是urllib模块)里面的一些机制来访问的
#			   所以如果网站判断出你不是通过正常的浏览器访问的，就会拦截你的请求
#			   比如我们的这个上个爬虫，网站看到的浏览器名称就是urllib，这个很明显就不是正常的浏览器
#			   
#			 我们如果反抗这种反爬虫机制那？通过伪装浏览器进行爬取
#			   就是说，我们改造我们的浏览器名称，把这个urllib改成正常的浏览器名称
#			   在浏览器里，开发者工具中，我们随便打开一个请求，找到请求头，请求头中有个user-agent(用户代理)
#			   这个user-agent就是我们要找的浏览器名称，我们模仿他就可以了，现在把它复制下来：
#			   Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
#			   这个信息就是表示我是用谷歌浏览器访问的，注意同一个浏览器的user-agent是一样的
#			   我们在发表说说时，电脑我们可以看到其他人使用的手机类型，这个类型信息，就储存在这个user-agent中
#			   如何使用这个user-agent？我们自定义浏览对象时，把指定的浏览器名称封装进去，就可以了
#			   那么如何封装那？需要用到字典了。还记得json吗？我们的json是不是就是一个类字典结构，可以用作前后端互相识别
#			   之所以用字典，是因为我们后期还需要用到很多头文件中的信息，我们要把他们放到一起，所以我们用到字典
#			   下面开始演示
#			



from urllib import request
import re

url=r"http://www.baidu.com/"

#创造字典，构造请求头信息。
#别忘了加引号，表示这是个字符形式。同时，因为这个太长，我们分成多行，用\进行连接
header={
	"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone \
	OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 \
	(KHTML, like Gecko) Version/7.0 Mobile/11B554a \
	Safari/9537.53"
}

#进行封装，我们要注意这个headers是个固定参数(形参)，不能改变，但是后面的header(实参)是自己命名的。没错，我们的形参和实参终于相遇了。
urll=request.Request(url,headers=header)

pachong=request.urlopen(urll).read().decode()

#print(pachong)

ree=r"<title>(.*?)</title>"

data=re.findall(ree,pachong)
print(data[0])

#这样就可以了，但是又有一个新的问题，那就是我们只使用了一个user-agent，这个看似没有什么问题，实际上，如果只进行一次爬取的话，的确没有问题
#但是在实际中，我们不可能进行一次爬取，或者说，我们的爬虫，要进行很大量的很集中的爬取，如果我们只有一个user-agent的话，我们很大概率会被拦截
#所以为了解决这个问题，我们应该使用多个user-agent，即，我们每次请求的时候，都随机的生成一个user-agent
#我们需要调用一个random模块，然后调用这个模块中的choice函数，这个函数能够随机选择一个列表中的一个值。
#我们创建一个列表，然后把这些user-agent放进去，接着使用choice函数随机这个值，并赋给一个变量，然后在封装的时候让headers等于这个变量就好了
#这里就不演示了