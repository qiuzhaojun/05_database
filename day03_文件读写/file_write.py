"""
文件写操作示例
"""

# 写方式打开文件
file = open("file.txt",'w')
# file = open("file.txt",'a') # 追加

# 写入内容
# n = file.write(b"hello world")
# print("写入了 %d 字符"%n)
# n = file.write("祝福祖国，节日快乐。\n".encode())
# print("写入了 %d 字符"%n)

# 将列表逐个写入
data = ["哈喽，死鬼\n","哎呀，干啥\n"]
file.writelines(data)


# 关闭
file.close()