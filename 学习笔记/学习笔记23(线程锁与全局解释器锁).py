import threading

lock=threading.Lock()  #创造一个线程锁(互斥锁),注意Lock的大小写
#线程锁的作用就是调用线程的时候，进入后进程就会被锁住，直到这个线程进行完毕才会打开。

num=100

def run(name):
	lock.acquire()  #设置线程锁
	global num      #设置全局变量
	num=num-1
	print('线程',num,'执行了，目前num的值为：',num)
	lock.release()  #释放线程锁

#创建并启动100个线程
for i in range(100):
	t=threading.Thread(target=run,args=(i+1,))
	t.start()

#全局解释器锁（GIL）
#不管系统CPU核心数量多少，都保证Python程序中同一时间点只能执行一个线程
#本意上是为了保证系统的数据安全的，但是我们可以通过线程锁可以解决这个问题。
#所以这个全局解释器锁是弊大于利的。为了解决这个问题，我们引用了多进程。

