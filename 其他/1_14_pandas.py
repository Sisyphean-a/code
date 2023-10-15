import pandas as pd

# 读取excel文件。header可以设置初始行，默认0，读取时会默认跳过空行
# header如果设置为None,则需要手动设置columns，否则自动生成数字
# 如果我们希望新的excel不自动生成索引列，可以在读取的时候加上一个index_col=""
people = pd.read_excel("./People.xlsx",header=0,index_col="ID")

# 获取文件中信息，得到的是行数和列数,类型是元组
print(people.shape,type(people.shape))

# 获取所有的列名
print(people.columns)
# 通过columns也可以直接生成一个列名，他会对文件直接进行修改
# people.columns = ["id","type",...]

print("===================")

# 获取头信息，默认为前五行，可以通过输入数字改变
print(people.head(3))

# 获取尾信息，默认为后五行
print(people.tail())
