'''ip地址127.2.2.1~192.168.255.255用于回路测试。
127.2.2.1可以代表本机IP地址，用http://127.0.0.1 就可测试本机中配置的web服务器
子网掩码：
每个IP地址都分割为网络号和主机号两部分，以便于IP地址的寻址操作
IP地址的网络号和主机号各有多少位？
如果不指定，就没有办法分辨哪个是网络号哪个是主机号，这就需要子网掩码来实现
子网掩码的唯一作用就是将某个IP地址划分为网络地址和主机地址两部分，所以子网掩码不能单独存在

TCP/IP协议是一个协议簇，可以用来表示很多协议，因为TCP/IP是其中最重要的两个协议，所以用它俩来命名

TCP和UDP区别
TCP协议（传输控制协议），是面向连接的协议，在收发数据之前，必须和对方建立可靠的连接，主要的是三次握手和四次挥手
UDP协议（用户数据报协议），是一个非连接的协议，不建立连接，所以效率高，可靠性低，一台服务机可以同时向多个客户传输相同的消息

使用ping IP 对方IP地址 就可以连接对方电脑

socket(简称套接字)是进程之间通信的一种方式，它能实现不同主机间的进程间通信，也是目前网络上大多数服务的基础，比如QQ等
socket技术是一种‘打开-读/写-关闭’的实现，服务器和客户端各自维护一个‘文件’。
在建立连接打开后，可以向自己文件写入内容供对方读取或者读取对方内容，通讯结束时关闭文件

socket可以说是一个文件，两方各有一个，每一个都有收取和发送两个功能，这两个功能可以实现通讯。'''


'''客户端：
import socket

#生成一个socket连接对象
client=socket.socket()

#和目标主机建立连接
#如果是连接本机，可以输入localhost
client.conect(('localhost',6969))

#然后就可以发送消息了，注意Python3中，没有办法直接发送字符，必须转换为二进制
#所以要在里面加一个命令，encode
client.send('hello world')

#关闭服务器
client.clost()




服务端：
import socket

server=socket.socket()

#绑定监听的对象
server.bind(('localhost',6969))

#监听，监听客户端的信息
server.lesten()
print('准备接电话。。。')

#等待消息,同时返回两个值
con,addr=server.accept()

print(con,addr)

#接收消息
#括号里面的参数是指你一次接收多大体量的参数，一般是1024字节
data=con.recv(1024)
print('接收到的消息：'，data)

#关闭server
server.close()
