#SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
#不允许十进制整数文本中的前导为零
#就是说数字类型的十进制的数字不能用01这样的格式，只能用1.
#把0删掉就行了
#IndentationError: unindent does not match any outer indentation level
#缩进错误：未缩进与任何外部缩进级别都不匹配
#注意Tab缩进和空格缩进不一样，可以用鼠标选中观察，点的是空格缩进，横线的是Tab缩进，而出现这个问题是因为两种缩进没有对齐
#也可以调整视图--缩进--使用空格缩进
#IndentationError: expected an indented block
#缩进错误：需要缩进的块
#检查一下代码的缩进是否有错误,我出现这个错误是因为选择语句中if和elif和else之间没有输出语句，所以它默认我缺少缩进
#加上print语句
#
#NameError: name 'weighe' is not defined
#之前我在if循环中使用and结构，结果老是出错，后来删去改成连续才解决问题
#
#AttributeError: 'set' object has no attribute 'items'
#出错原因是在http请求的header里，应该用冒号而不是逗号