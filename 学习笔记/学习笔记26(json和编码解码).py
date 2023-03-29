#json数据结构
#用来做数据传递，可以在前端和后端之间，或者不同语言之间，不同系统之间进行传递
#json就是js中的对象
#js(JavaScript:一种前端语言，和Java没有什么关系，单纯的就是当年Java比较火，蹭热度。后来，就火了)
#结构形式如下
#{key:value,key,value.....}
#这不是字典吗？
#在Python中字典经常用来做Python和json的对象转换
#本质上讲，json就是有特定结构的字符串。
#

import json

#json转字符
j='{"city":"北京","name":"熊猫"}'
#这个结构就是Python中长得像字典的字符串
#加一个单引号就可以转换了

print(type(j))
print(j)

#转为字典
p=json.loads(j)

print('\n',type(p))
print(p)

#字典转json
dictt={"city":"北京","name":"熊猫"}
ss=json.dumps(dictt)
print('\n',ss)
#我们发现字典里面的值转成了一种编码格式ASCII
#我们可以加入一句话，让他不要转换编码格式
ss=json.dumps(dictt,ensure_ascii=False)  
#ASCII码是美国信息交换标准码（American Standard Code for Information Interchange）
#这就话就是不要保持ASCII码
print('\n',ss)
print(type(ss))



#编码和解码
#encode()  decode()  #一个编码，一个解码
#我们的计算机识别的是二进制，但是我们编的不是二进制，为了让我们电脑看懂，需要转换为二进制
#ASCII编码方式支持阿拉伯数字和英文还有一些英文符号
#中国出来了两个编码方式，分别是gb2312和gbk(GB:中国标准，或者说国标)，用来专门处理中文
#后来出来一个国际的编码标准，叫做unicode
#后来对这个unicode进行改进，这个改进的结果，叫做utf-8，这两个基本支持全世界所有语言

#Python中默认以unicode作为编码格式的
#在我们实际编码过程中，一般都是对字符串做这个编码处理的
#Python3中的字符串分为两种形式，一种是str，存储unicode类型，一种是bytes，存储byte(二进制)类型

#把byte类型转换为str类型叫做解码，反过来叫做编码
#我们一般看的是str类型

a="我爱天安门"
b=a.encode("utf-8")  #编码，转成字节码
print(b)

c=b.decode("utf-8")  #解码，转成字符串
print(c)

#如果我们之前用的编码形式是gbk，我们解码的时候也要用gbk，即：编码方式和解码方式必须相同