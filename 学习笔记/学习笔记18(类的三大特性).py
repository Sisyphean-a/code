#类的三大特性
#特性1.类的封装
class Card(object):
	
	def __init__(self, num,pwd,ban):
		self.num = num #卡号
		self.pwd = pwd #密码
		self.__ban = ban #余额  注意！这一加了两个下划线，表示的是私有属性
						 #私有属性只能在类的内部被访问 

	def cun(self):		
		print('存款')

#	def getBan(self):		#如果没有这句话，后面的print(card.__ban)就无法输出结果
#		return self.__ban   #这句话就是在类的内部被访问的，所以可以用它输出结果
							#所以我们用return返回这个__ban值，于是这个值我们就可以通过调用这个方法显示出来了
							
							#我们也可以在这方法里面使用这个私有化，同样是加两个下划线
							#不过如果真的想加安全，这个方法是用处不大的，所以建议用其他语言建立安全系统
		
	def getBan(self,numm,pwdd):
		if numm==self.num and pwdd==self.pwd:
			return self.__ban
		else:
			return '输入错误！'





card=Card('1001','123456',1000) #开卡

#print(card.ban)



print(card.getBan(111,111))	#这个是输出方法，所以需要加上括号

print(card._Card__ban)#这个就可以直接输出结果不需要验证



#特性2.类的继承
#类具有层级关系，层次高的包含的东西更多，比如狗类，它是一个类，但是它属于动物类，这就是说，狗类继承自动物类
#这是一个类与类的上下关系，我们用类的继承来表示一个层级关系，但是要注意，虽然一个类继承自另一个类，但是它本身依然是个类
#
class Animal(object):

	def __init__(self, color):

		self.color = color
		
	def eat(self):
		print('动物在吃')

	def run(self):
		print('动物在跑')



class Cat(Animal):  #这里括号里面的内容发生了变化，还记得上一节课中，我说object的意思是Classname继承自object类
					#那时候不懂，现在就可以理解了，就是说这个猫类继承自上面的动物类
					#这个猫类的父类就是上面的动物类
					#
		pass 		#我在这里直接跳过初始化和普通方法，下面直接开始实例化
#cat=Cat()			#注意这个运行的结果，TypeError: __init__() missing 1 required positional argument: 'color'
					#缺少1个必需的位置参数:“color”，哎，这个类我们没有给它定义属性，为什么会出现缺少参数？
					#原因就是它是继承自它的父类Animal的，所以这个Animal里面定义的属性，这个猫类也自然拥有
					#就仿佛，我们定义了什么是动物，如何定义的？是不是找出所有动物都共有的属性，然后赋值给它
					#所以这个猫尽然是动物类，就必然也拥有这些属性，这个，就是类的继承
					
#所以我们要想实例化，就需要换换格式
cat=Cat('黑白相间')
print(cat.color)	#这样就可以了，同样，我也可以直接调用它的方法

cat.eat()
cat.run()

class Dog(Animal):

	def __init__(self, name,age,color):

		super(Dog, self).__init__(color)#这句话的意思比较复杂，首先super在这里是父类的意思，这个命令的意思就是调用父类的__init__方法
										#如果没有这句话，上面color就相当于重新定义一次初始化方法，而不是从父类调用
										#这样就可以调用父类的初始化方法了。
		self.name = name
		self.age = age

	def eat(self):
		print('狗在啃骨头！')

#dog=Dog('小黑',10)  #注意，这个传进去的数据是子类的属性，当父类和子类都具有初始化属性时，会优先考虑子类的信息
dog=Dog('小黑',10,'白色')
print(dog.color)    #可以观察到，上面我们并没有使用self.color = color，但是他却成功输出了数据，是应为我们上面调用了父类的方法，
					#而父类，有self.color = color语句
							
dog.eat()			#同样，方法也是如此,但是如果没有子类没有这个方法，它会去调用父类的方法，如果父类也没有，就只能报错了


#特性3.类的多态
#Python中严格来讲，是没有多态的，只是形式上类似多态
#多态的意思是一个类拥有多种形态，或者说，一个对象拥有多种形态
#多态的用法
def feed(obj):
	obj.eat()					#我定义的这个eat指的是哪一个？这是一个方法，但是前面有两个类都有eat
								#这个obj可以识别我输入的参数是哪一个，从而赋相应的值给它，比如后面我输入an或dog		

an=Animal('黄')					#对象是可以最为一个参数传到函数里面的
dog=Dog('小黑',2,'白色')			#多态的作用就是综合赋予方法，如果有多个类，我只需要设置一个方法再用多态表示就可以了
								#意思就是对于多个类中的相同方法，我不需要输入多次，只需要输入一次就可以了	
feed(an)
		
