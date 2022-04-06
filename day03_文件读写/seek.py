"""
文件偏移量
"""

f = open('file.txt','wb+')

f.write(b"Hello world")
f.flush() # 文件有内容

print("文件偏移：",f.tell())

# 操控文件偏移量
f.seek(-5,2)

data = f.read()
print(data)

f.close()
