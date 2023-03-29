#函数的定义
#函数其实就是一种方法，需要调用才能有价值
def square(x):         #def是关键字，作用是告诉电脑我要定义一个函数。
					   #square是定义的函数名，x是输入参数
	s=x*x			   #这是函数主体，是用来说明函数的内容
	return s  		   #return是返回变量
	#至此，函数命名成功

#简单调用函数
def h1(a):
	print('函数h1被执行了')

h1('666')		#调用方法：h1内的666首先赋值给a，然后开始执行你定义的函数，
				#如果你没有输入参数，调用的时候你也没办法赋值函数.

#return关键字
def add(a,b,c,d):
	e=a+b+c+d
	#return e

result=add(36,15,48,65)  #add(36,15,48,65)的结果就是那个返回值，如果没有return的话，
						 #输出的结果就是None，说明没有结果。add的意思是运行了命令，但是命令里面没有
						 #print，所以没有输出，你只是运行了函数。为了让结果能够在需要的时候输出来，
						 #你需要加一个返回变量return，意思是把结果返给add(36,15,48,65)
						 #所以这一个函数的完整路线应该是：
						 #add--def--e--ruturn--add--result
						 #
print('本次相加的结果',result)	



print('\n')
def zzj(x):									#f在这里类似于y=ax+b的变量x，而zzj(f)其实就是f(x)
	if x=="苹果" or x=="梨子" or x=="葡萄":  #
		print('正在榨汁！')					#
		print('两分钟后。。。。')				#
		zhi='一杯'+x+'汁'					#这里的zhi就相当于y，里面的一杯和汁就相当于a和b
		return zhi							#这个return其实就相当于一个等号，使f(x)=y
	else:									#这是我能想到的最好解释了。如果你不让f(x)=y,那你后面的赋值就毫无意义，因为f(x)是没有结果的
		print('榨汁机要坏了！')

guozhi=zzj('葡萄')

print(guozhi)