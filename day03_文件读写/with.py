"""
with 打开文件
"""

# 通过with语句打开文件
with open("file.txt",'r+') as f:
    f.write("hello kitty")
    data = f.read()
    print(data)

# 语句结束 f 会被自动释放
