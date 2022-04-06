"""
空洞文件
"""

f = open("file.txt",'wb')

f.write(b"begin")
f.seek(1024,2)
f.write(b'end')

f.close()