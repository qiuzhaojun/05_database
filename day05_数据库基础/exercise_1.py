"""
基于 log.txt文档
编写一个函数传入一个端口的名称，返回这个端口
对应的 address值
address is  10f3.116c.e6a7

提示： 每段之间有空行
    每段的收个单词是端口名称
    有的段没有这个值，或者端口传错的情况

"""
import re

# 提取出每段文字 --》 生成器
def get_info():
    file = open('log.txt','r') # 读方式打开
    while True:
        # 每次while循环info就获取一段内容
        info = ""
        for line in file:
            if line == '\n':
                break
            info += line # 累加一段的内容
        # info 为空说明到了文件结尾
        if not info:
            file.close()
            return
        else:
            yield info # 提供这一段内容


# 匹配想要的内容 port--> 端口名称
def main(port):
    # 通过生成器获取每段内容进行对比
    for info in get_info():
        # 是否为想要的段
        obj = re.match(r"\S+",info)
        if port == obj.group():
            # 匹配address is 地址
            pattern = r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            result = re.search(pattern,info)
            if result:
                return result.group()
            else:
                return "Unknown"
    return "没有该端口"

print(main("TenGigE0/0/2/1.12"))