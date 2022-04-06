"""
os模块 文件处理小函数
"""
import os

# 获取文件大小 bytes
# print(os.path.getsize("./笔记.txt"))

# 获取目录下的内容
print(os.listdir("/home/tarena"))

# 判断文件是否存在 True False
print(os.path.exists("./04.txt"))

# 判断一个文件是否为普通文件 True False
print(os.path.isfile("./4.txt"))

# 删除文件
# os.remove("笔记.txt")
