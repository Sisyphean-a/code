import requests
from lxml import etree
import re


text='''
qyhw奇奕画王v3.0中文安装版(前身是金山画王)

qyhw.7z  29.2MB

下载链接：https://www.lanzoui.com/iu23qiz3hra

已纳入个人淘专辑：https://www.52pojie.cn/forum.php?mod=collection&action=view&ctid=2124

金山画王的最后一个版本就是2006，后续版本已更名为奇奕画王（金山画王本就是金山公司OEM南京奇奕科技开发的软件），并且进行收费。

安装方法：
先运行setup.exe安装原版，再覆盖主程序flymain.exe。注意该补丁为永不过期补丁，即程序将一直处于240天的试用期，且永不过期。
ps：有小盆友的可以下载个玩玩，系统日期调到2021.12.2还可以运行，其它的未测。不喜勿喷。
2006版的金山画王可以在此下载：链接: https://pan.baidu.com/s/1keVGKBECC2OAdWvXrBJfKQ 提取码: 6yc9
https://ws28.cn/f/44h2n5jgqcu

'''





#re=re.findall(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]',text)
re=re.findall(r'(^https|http.*)',text)
print(re)




#//*[@id="pid35305644"]/tbody//div[@class="t_fsz"]
