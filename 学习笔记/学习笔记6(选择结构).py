#选择结构
#if结构           
#if 判断条件：    #如果是，则执行1，如果否，则执行2（只是一个布尔值）
#   执行语句1     #这里需要有缩进，表示执行条件在if之下
#else:
#   执行语句2
#
#
#单条件判断语句
#注意事项：1.两个函数后面都要有：(冒号)，来表示延伸
#         2.同时else后面不加条件，它只是用来收集余集
cunkuan=120
if cunkuan>100:
	print('可以买宝马')
else:
	print('还是骑自行车吧')
#
#
#多条件判断语句
#elif，表示其他条件
if cunkuan>60:           #注意：两个if表示两个判断，互不影响
	print('买丰田')       
elif cunkuan>30:         #elif可以做使用多次，但else一个if中只能使用一次
	print('买二手车')
elif cunkuan>20:
	print('其实叫滴滴也不错')
else:
	print('咦！我的破自行车那？')
#另外，如果你的if下面的执行语句暂时没有想好，可以先输入pass来代替。
#
#
#if嵌套结构
#在一个判断结构if中再加一个判断结构if
zizhu=20
if cunkuan>100:
	print('可以买宝马')
	if zizhu>50:
		print('宝马740')
	elif zizhu>30:
		print('宝马520')
	elif zizhu>20:
		print('宝马320')
	else:
		print('二手宝马')
elif cunkuan>60:           
	print('买丰田')       
elif cunkuan>30:        
	print('买二手车')
elif cunkuan>20:
	print('其实叫滴滴也不错')
else:
	print('咦！我的破自行车那？')
    #这里之前出了一个问题，我标记一下
    #IndentationError: unindent does not match any outer indentation level
    #就是这个，问题是看不到的，其实就是一个缩进的问题，它区分空格缩进和tab缩进，两者不一样
    #只是个很小又很麻烦的问题，找了半天才解决，解决方法是调节缩进一致
    #视图--缩进--使用空格缩进
    #这样就可以了，但还需要把之前的手动修改一下