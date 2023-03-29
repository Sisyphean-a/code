#第一个：
#urllib
#这个就是大名鼎鼎的用来做爬虫的模块
'''from urllib import request    #这就是调用了request包

url='http://www.baidu.com'
data=request.urlopen(url).read() 
print(data.decode())    	'''	 #decode:译码，作用是对结果进行编码，变得可看一点

#import os			#这是一个控制操作系统的模块
#os.system(r'D:\eDiary\eDiary.exe')		#这个是打开一个文件，不过要注意，这里有转义字符，需要使用r消除转义
#os.rename(r'C:\Users\普罗米修斯\Desktop\新建文件夹\pip的说明书.txt',r'C:\Users\普罗米修斯\Desktop\新建文件夹\pip说明书.txt')		
#这个是对文件进行重命名，左边输入路径，右边输入想改的名字'''

import webbrowser #这个是控制浏览器的模块
webbrowser.open('http://www.baidu.com')#打开指定网站