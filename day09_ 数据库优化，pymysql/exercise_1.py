"""
创建一个数据库 dict
创建一个数据表 words
id   word  mean

将dict.txt单词本中单词插入到该数据表

create database dict;
create table words (id int primary key auto_increment,word varchar(30),mean varchar(1024));
"""
import pymysql
import re

# 生成数据库连接对象,连接数据库
database = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

db = pymysql.connect(**database)

# 生成游标  游标:操作数据库数据,获取操作结果的对象
cur = db.cursor()
file = open("dict.txt")

# 使用executemany ---> [(word,mean),(),...]
l = [] # 存储单词
for line in file:
    tup = re.findall(r"(\w+)\s+(.*)",line)
    l.append(tup[0])
try:
    sql = "insert into words (word,mean) values (%s,%s);"
    cur.executemany(sql,l)
    db.commit()
except:
    db.rollback()

# 关闭游标和数据库链接
file.close()
cur.close()
db.close()