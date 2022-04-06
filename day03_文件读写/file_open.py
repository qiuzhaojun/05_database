"""
打开文件 示例
"""

# 打开文件
# file = open("file.txt",'r') # 文件必须存在
file = open("file.txt",'w') # 不能存在创建
# file = open("file.txt",'a') # 追加

# 读写文件
print(file)

# 关闭文件
file.close()
