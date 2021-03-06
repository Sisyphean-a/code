#面向对象，之前的是面向过程，所谓面向过程，就是需要依次进行的方式
#关于对象，有以下几个概念
#概念：对象，类
#属性，方法
#封装，继承，多态
#
#对象具体，类模糊。
#类是有共有特征构成的，而对象则具有独有特征
#所谓特征，就是属性
#它们的功能就是方法（也就是函数）
#
#接下来就创建一个类
#
class Perple(object):				#class是类的含义，也是类的创建符号。
									#后面的Perple是类名，自定义，注意，类名的首字母必须大写
									#object的意思是Classname继承自object类，也可以继承其他的类(反正我目前是不懂)
									#
	"""docstring for Perple"""  	#这是备注

	life='生活'						#类变量(类属性)，直接定义在类的下面

#先定义属性
#__init__函数：初始化方法     
	def __init__(self,name,kind,gender):	#def __init__(self,  ）这一部分是不可变的，是规格化的。__init__是函数名
											#但是self后面的是可变的，可以自定义内容和数量，也就是属性
											#这句话的意思呢，一点一点来，首先是创造一个函数，这个函数名叫做__init__
											#然后这个__init__函数的的第一个词是实例对象，后面的属性就是赋予给实例对象的属性
											#self指的是类实例对象本身(注意：不是类本身)，就是下面的实例对象(当前对象)，同样这也是可以修改的。
											#
		self.kind = kind					#嗯，这一句就很有趣了，自己指向自己？不是的，这里并没有要求他们相等，主要是一种约定俗成
		#实例变量(实例属性)					#前一个我的一个
		self.gender	= gender				

		self.name = name
											#
#再定义方法
#这个函数叫普通方法
	def job(self):					#这个是定义方法	
		print('人类是为了通过工作来改造这个世界的，而人类得到的满足感是时代给予的奖励')

	def multiply(self,think):
		print(self.gender,'需要繁衍来完成时代的任务，是不是像一个生物体的细胞',think)

		
#实例化
#类是抽象的，我要想运行这个类，必须指明对象，这就是实例化，类比于人类中的确切的那个人
#实例化对象：对象名=类名(参数列表)
friend1=Perple('黄松科','黄种人','男性')		#这里还有一个参数未显示，就是self，这是隐式传入
friend2=Perple('胡强强','黄种人','男性')		#对应关系：这里的黄种人对应了上面初始化的kind
											#同样的，其他的也一一对应，只有一个self，似乎没有对象可以对应
											#是有的，与self对应的是friend1，friend2


#作用:1.输出数据，访问属性
print(friend1.name)
#2.修改变量
friend2.kind='非洲人'
print(friend2.name,'是',friend2.kind)
#3.调用方法
friend1.job()		#这里其实默认传了一个参数'self'，这个self就是这一行的friend1本身
					#也可以自己定一个参数，在定义方法里面设定
friend2.multiply('当然我不会这样想')			

#这里进行一次总结，关于这个类
#首先就是它是面向对象的，与之前面向过程的不同，它可以在一定程度上脱离顺序
#然后就是它的结构，先创建一个类，使用class创建。
#接着定义这个类的属性，这个过程叫做初始化。其意思就是赋予这个类一些共有属性
#接着是定义这个类的方法，给这个类赋予一些功能，其实就是告诉我们它能干什么
#最后就是应用了
#应用的方法也有要求，首先就是要先进行一个定位或者说指明，这个说明对象的过程叫做实例化
#实例化的作用是赋予那些属性以含义，使初始化的属性具有特殊性，或者说具有‘个人色彩’
#然后就可以进行应用了，可以去查看你赋予的属性值，可以修改你赋予的属性值
#当然，最重要的是你可以去调用这个类的功能，也就是调用方法
#然后，这一节就到这吧
print(int('001001',2))