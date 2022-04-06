"""
pymysql 数据库处理结构示例
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

# 数据操作


# 关闭游标和数据库链接
cur.close()
db.close()


