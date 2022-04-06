"""
练习1： 基于单词本完成
编写一个函数，传入一个单词，返回单词对应的解释

提示：  每行一个单词
       单词与解释之前有空格
       单词按顺序排列

       split()
"""

def find_word(word):
    file = open("dict.txt") # 读打开

    # 查找单词
    for line in file:
        # 提取单词和解释
        tmp = line.split(' ',1)
        # 如果遍历到的单词已经比目标单词大，则结束查找
        if tmp[0] > word:
            file.close()
            break
        # 找到单词
        if word == tmp[0]:
            file.close()
            return tmp[1].strip()

print(find_word("marry"))








