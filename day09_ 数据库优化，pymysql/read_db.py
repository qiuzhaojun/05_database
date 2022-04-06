"""
数据库读操作实例
"""
import pymysql

# 生成数据库连接对象,连接数据库
database = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}

db = pymysql.connect(**database)

# 生成游标  游标:操作数据库数据,获取操作结果的对象
cur = db.cursor()

# 去读数据库内容 select
sql = "select name,age,score from cls where score>90;"
cur.execute(sql)

# 迭代法获取记录
# for row in cur:
#     print(row)

# 获取一个查询记录
one = cur.fetchone()
print(one)

# 获取多个查询记录
many = cur.fetchmany(2)
print(many)

# 获取所有查询记录
all = cur.fetchall()
print(all)


# 关闭游标和数据库链接
cur.close()
db.close()