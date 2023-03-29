import threading
import time

def run(name):
	print(name,'线程执行了！')
	time.sleep(5)


#程序执行时，程序本身就是一个线程，叫主线程
#手动创建的线程叫子线程
#主线程的执行不会等待子线程执行完毕，启动之后就会直接执行后面的代码、
#
#创建线程
t1=threading.Thread(target=run,args=('A',))  #target是目标的意思，意思是在这个线程中执行那个方法
t2=threading.Thread(target=run,args=('B',))  #args是固定用法，这一步的意思是传入参数。如果有一个参数就传一个参数，但是要加一个逗号。
											 #其实括号里面的就是说，这个线程是谁，以及调用这个线程所需要输入的内容。这，就是调用线程

t1.start()  #启动线程
t2.start()

t1.join()  #设置子线程
t2.join()

print("执行完毕！")


