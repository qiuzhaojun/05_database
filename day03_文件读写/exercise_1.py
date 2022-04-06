"""
求100000以内质数之和
"""

# 判断一个数n是否为质数
def isprime(n):
    if n <= 1:
        return False 
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

# num以内的质数之和
def prime_sum(num:int):
    prime = [] 
    for i in range(num + 1):
        if isprime(i):
            prime.append(i) # 是质数加到列表中 
    return sum(prime) # 求和


print(prime_sum(100000))














