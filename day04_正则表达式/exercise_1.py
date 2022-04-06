"""
现在有两个文本文件（自己指定），
编写一个程序将两个文件合并为一个新的文件
"""

# 分拷贝文件
def copy(filename,fw):
    """
    filename: 要拷贝的文件
    fw: 文件对象，向fw中去写
    """
    fr = open(filename,'rb')
    # 文件复制
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()

def union_files(filename,filelist):
    """
    :param filename: 要合成的文件
    filelist : 要拼接的文件列表
    """
    fw = open(filename,'wb')
    # 拼接两个文件
    for file in filelist:
        copy(file,fw) # 拷贝文件
    fw.close()

if __name__ == '__main__':
    filelist = [
    '../day01/1.txt',
    '../day02/2.txt',
    '../day03/3.txt'
    ]

    union_files('./笔记.txt',filelist)