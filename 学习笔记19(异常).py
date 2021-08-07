a=[11,5445,6,64,55,'a',4,0,15,56,95]
for i in a:
	print('......',i)
	#处理异常，使用try关键字，可以使用跳过异常
	#
	try:            			#写可能会报错或出现异常的代码
		print(3/i)
	except Exception as e:		#捕获try里面的异常，Exception就是捕获到的异常对象
		print('出错了！',e)				#出现异常时执行的语句
	else:
		print('正常')			#没有异常时执行的语句
	finally:
		print('本次结束')		#无论是否异常，都要执行的语句,可以用来做我们程序的结尾工作，比如IO程序的关闭


#同时我们可以自己设置异常
pwd='123456'

if len(pwd)<8:
	ex=Exception('密码不能低于八位数！')
	raise ex	#抛出异常

else:
	print('密码设置成功')
