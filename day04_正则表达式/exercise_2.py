"""
编写一个函数，传入一个文件夹，删除掉该
文件夹中 小于 100kb的普通文件。
"""
import os

def remove_file(dir):
    # 获取文件列表 file只是文件名
    for file in os.listdir(dir):
        # 判断是否为普通文件并且<100kb
        filename = dir + '/' + file
        if os.path.isfile(filename) and \
                os.path.getsize(filename) < 1024:
            os.remove(filename) # 符合则 删除

if __name__ == '__main__':
    remove_file("/home/tarena/qtx")
