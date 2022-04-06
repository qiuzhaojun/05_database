"""
缓冲实验 演示
"""

# 设置行缓冲
# f = open("file.txt",'w',buffering=1)

# 指定缓冲大小 必须要二进制方式打开
f = open("file.txt",'wb',buffering=10)

while True:
    data = input(">>")
    if not data:
        break
    f.write(data.encode())
    # f.flush() # 刷新缓冲

f.close()