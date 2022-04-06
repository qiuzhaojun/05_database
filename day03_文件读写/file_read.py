"""
读取文件示例
"""

# 打开文件
file = open('file.txt','r')

# 读取文件
# 不加参数表示读取所有内容 加参数表示读取一定的字符数
# data = file.read(6)
# print(data)
#
# data = file.read()
# print(data)

# 对于大文件 建议循环读取，而不是一次性读取
# while True:
#     # 当文件读取完 再次read会返回空子串
#     data = file.read(5)
#     if not data:
#         break
#     print(data,end='')


# 每次读取一行内容
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)

# 读取多行 将每行内容 分别放在一个列表中
# data = file.readlines(38)
# print(data)


# for循环取每一行  读方式文件自带迭代属性
for line in file:
    print(line)


# 关闭文件
file.close()
