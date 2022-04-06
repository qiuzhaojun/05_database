"""
数据库写操作示例
1. 不支持事务的引擎 execute 会直接执行语句生效
2. 支持事务的引擎 写操作会默认开启事务
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

# 写操作示例 insert delete update
try:
    # sql = "update cls set score=99 where id=1;"
    # name = input("Name:")
    # sql = "update cls set score=100 where name='%s';"%name
    # print(sql)

    # 通过 execute第二个参数给sql传递数值
    name = input("Name:")
    sql = "update cls set score=%s where name=%s;"
    cur.execute(sql,[97,name])
    db.commit() # 事务提交
except Exception as e:
    print(e)
    db.rollback() # 事务回滚

# 关闭游标和数据库链接
cur.close()
db.close()