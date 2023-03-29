#第三方模块
#所有的第三方模块都安装在python安装目录下面的Lib中的site-packages中
#如何安装第三方模块
#下载方式有两种，一种是pip工具
#
	#pip工具：第一次使用的话需要升级pip工具，如何升级？在命令提示符中输入以下命令
	#python -m pip install --upgrade pip   #upgrade是升级的意思，install是安装的意思
	#
	#升级之后，在提示符里就可以使用pip下载模块了，输入格式如下
	#pip install 包名
	#回车就可以下载了
	#
	#pip也可以显示所有安装好的包，格式如下
	#pip list
	#
	#也可以卸载一个模块
	#pip uninstall 包名
	#卸载的时候计算机会询问proceed(y/n)?输入y确定卸载即可
	#
#另一种是在网上安装
#
	#使用https://www.lfd.uci.edu下载
	#https://www.lfd.uci.edu/~gohlke/pythonlibs/
	#里面的cp代表的是python版本
	#下载之后会得到一个扩展名为.whl的文件
	#在命令提示符中找到文件位置，然后使用pip install 文件名
	#回车安装
	