import datetime

now=datetime.datetime.now()

print(now)
#打印结果是系统的当前时间2019-12-05 16:29:31.256917

#也可以获取一个指定日期
d=datetime.datetime(2019,10,1,1,1,1)  #参数分别是年，月，日。当然也可以加上时分秒
print(d)

#日期转字符串
now1=datetime.datetime.now()
d=now1.strftime("%Y-%m-%d %H:%M:%S")    #指定格式，分开来写，str,f,time。日期转字符串
				                       #括号里面是转换的格式，冒号里面的符号怎么显示都可以，但是那个大小写不能动，我也不懂。
print(type(d))
print(d)

#字符串转日期
s="2020-8-15 2:30:18"    #这是一个字符串
d=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")  #这个格式化要保证与前面的s保持一致


'''
#当然，我们也可以用和上面日期转字符串相似的书写方式,就是有点丑
now2=datetime.datetime
d=now2.strptime(s,"%Y-%m-%d %H:%M:%S") 
'''


print(type(d))
print(d)