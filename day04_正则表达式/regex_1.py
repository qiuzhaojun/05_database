"""
正则表达式 re  示例
"""
import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(\w+):(\d+)"

# 有子组的时候函数只返回子组对应的内容，而不是正则匹配到的内容
# result = re.findall(pattern,s)
# print(result)

# 使用正则表达式匹配到的内容切割字符串s
# result = re.split("\W+",s,2)
# print(result)


# 使用 ## 替换正则表达式匹配到的内容，返回替换后的字符串
result = re.sub("\W+",'##',s,2)
print(result)












