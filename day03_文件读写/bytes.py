"""
字节串示例
1. 是否所有的字符串都能转换为字节串  是的
2. 是否所有的字节串都能转换为字符串  不是
"""

name = "Emma"
print(type(name))

# ascii字符定义字节串
name = b"Emma"
print(type(name))
print(name)

# encode() 将字符串转换为字节串
name = "张无忌".encode()
print(type(name))
print(name)

# 将字节串转换为字符串
print(name.decode())