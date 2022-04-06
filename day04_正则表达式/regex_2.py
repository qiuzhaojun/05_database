"""
正则表达式 re  示例 2
"""

import re

# 目标字符串
s = "Alex:1996,Sunny:1997"
pattern = r"(?P<name>\w+):(\d+)"

# 匹配目标字符串，只匹配第一处
result = re.search(pattern,s)
# 获取捕获组字典 {组名:对应内容}
print(result.groupdict())


# # 匹配目标字符串的开始位置
# result = re.match(pattern,s)
# # 通过group传参可以获取指定子组的对应内容
# print(result.group('name'))

# # 匹配到的内容形成一个可迭代的对象
# result = re.finditer(pattern,s)
#
# # 每次迭代取出一处匹配内容
# for i in result:
#     # match对象
#     print("匹配内容对应位置:",i.span()) # s[0:9]即对应内容
#     print("匹配到的内容:",i.group())