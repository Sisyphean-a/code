#容器
#
#
#2.元组
#元组用tuple表示，元组与列表相似，但元组中的元素是不可变不可修改的。
#元组用小括号
tuple=(3.14,5,6,666,'aaa','你好')
print(tuple)
#元组也可以切片
print(tuple[3:5])
#元组的意义是禁止修改，例如圆周率是3.14，如果改变就可能出错。
#
#
#3.字典
#字典用在需要高速查找的地方，在其他语言中被称作哈希映射或者相关数组
#里面的每一个元素都有一个对集，一个叫键，一个叫值，通过键可以寻找到值
dict={'name':'张三','age':22,'time':'2019年10月28日11:28:14'}#字典的键是不可以重复的
print(dict)
print(dict['time'])#注意字典是不可以检索的
#
#
#4.集合
#集合其实也是一种字典
#集合是一组键的集合，只有键没有值,所以没有重复值
#没有重复值就可以去重
#集合有两种定义方式，第一种时使用花括号,第二种是使用set()函数
print('\n4.集合')
a={1,2,3,4,5,"上山到老虎"}
b=set([1,2,3,4,5])
print(a,b)
#例如
print('去重')
list1=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5]
c=set(list1)     #这一句的意义是去重，但结果是个集合，输出一下试试
print(c)         #运行的结果就是带大括号的集合
d=list(c)        #这句话的意义是让集合转换为列表
                 #注意，所有的已经被定义的函数再次使用就只能做赋值讲
                  #所以为了使这个list能够使用，前面就不能使它赋值
print(d)         #这样我们就得到了一个不重复的列表

#集合的差集
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
print(a-b)      #即a中含b的都被删去了
#集合的并集
print(a|b)      #|的意思是或者，这句的意思是a或者b
#集合的交集
print(a&b)      #意思是输出a和b都有的元素
#集合的对称差
print(a^b)      #意思是输出两者非共有的，其实就是差集
