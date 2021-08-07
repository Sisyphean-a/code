#模块是python中的最高级别组织单元，它将程序代码和数据封装起来以便重用。
#模块的作用：
#1.代码重用
#2.实现共享服务和数据
#
#导入从本质上讲，就是在一个文件中载入另一个文件，并且读取它。主要读取的是它的函数
#打开模块的位置，找到安装的python文件，里面的lib里面就是。
import random		#import的意思是引用一个模块,random是一个生成随机数的模块
					#import的汉语意思是导入
a=random.random()	#前一个random是上面调用的模块，后一个random是函数，中间的.是调用函数
					#这句话的意思就是模块random调用自己的函数random
					#这句话的作用是随机生成一个0到1之间的任意数值
print(a)
#上面的三句话，第一句是调用一个模块，第二句是调用模块的一个函数。
#
#
b=random.choice(['张三','李四','王五','赵六'])	#choice的汉语意思是选择
												#choice就是在给定的列表中随机调用值,注意列表的格式
												#也是一种随机调用，只不过是给定值的调用
												#可以用来做随机检测
												#这是一个使用很多的模块
print(b)

#一个模块可以含有多个函数
#代码重用的意思就是不需要你去再创造函数，可以直接使用已经定义好的函数（是不是和内置函数一样）
#很多功能别人已经写好并封装到一个模块里面，你只需要调用就好了
#

#模块导入
#仅调用模块里的某个函数
from random import choice 			#这句话的意思是从random中调用choice这个函数，同时因为直接指明了函数，所以其他函数就不可以调用了

print(choice([1,2,3,4,5,6]))		#如果是直接调用模块里的函数，就不需要指明模块了(random.random())
#print(random())					#因为没有办法调用其他函数了，所以系统会报错
									#TypeError: 'module' object is not callable，意思是这个random不可调用
#print(random.random)				#这个也没有办法调用

#也可以引用一个模块的多个函数，只需要在后面用逗号连接就行了
from random import choice,random 	#这个就可以执行random函数了


#也可以调用所有的函数，加一个*号就可以了
from random import *
#那么from random import *和直接impot random有什么区别那？
#如果是impot random,下面的函数前面就需要加一个random.指明模块
#如果是from random import *,下面的函数直接用就可以了，不需要加random.
#

#randint函数
#随机生成一个指定范围的整数
print(randint(1,100))


#如何调用自己编写的模块
#假如说在一个文件（text1.py）中编写了一个函数f1()
#def f1():
#    print('调用f1n被执行了')
#    
#在另一个文件中，
#import text1
#text1.f1()
#
#这就可以了，下面我们调用一下试试



#需要注意的是：我们调用的模块的文件名必须是符合规定的，
#我的本意是调用之前的学习笔记，但提示语法无效SyntaxError: invalid syntax
#我改用其他的文件，因为懒，文件名是1和2，结果再次报错
#我查了很多资料，没有一个能解释这种情况，最后自己悟了。。。规范啊！
#
#
#这里给一份命名规范
#Python推荐命名规范：
'''模块名和包名采用小写字母并且以下划线分隔单词的形式；
如：browser_driver
类名或异常名采用每个单词首字母大写的方式；
如：BasePage, KeyboardInterrupt
全局或者类常量，全部使用大写字母，并且以下划线分隔单词；
如：CONSTANT_NAME
其余变量命名包括方法名，函数名，普通变量名则是采用全部小写字母，并且以下划线分隔单词的形式命名。
如：my_func
以上的内容如果是内部使用的，则使用下划线开头命名。
如：_verify_status, _num, _ClassName'''
