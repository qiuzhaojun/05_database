"""
数据库写操作示例
"""

import pymysql

# 生成数据库连接对象,连接数据库
database = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}

db = pymysql.connect(**database)

# 生成游标  游标:操作数据库数据,获取操作结果的对象
cur = db.cursor()

# 批量写操作实例
l = [
    ("Dave", 16, 'm', 81),
    ("Ala", 17, 'w', 76),
    ("Levi", 19, 'm', 89),
    ("Han", 16, 'w', 80)
]
sql = "insert into cls (name,age,sex,score) " \
      "values (%s,%s,%s,%s);"
try:
    # for row in l:
    #     cur.execute(sql, row)

    # 等同于上面的循环
    cur.executemany(sql,l)
    db.commit()
except:
    db.rollback()

# 关闭游标和数据库链接
cur.close()
db.close()
