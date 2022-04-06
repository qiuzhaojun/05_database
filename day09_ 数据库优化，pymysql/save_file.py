"""
二进制文件存储
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

# 插入二进制文件
# with open('timg.jfif','rb') as f:
#     data = f.read()
#
# sql = "update cls set image=%s where id=1;"
# cur.execute(sql,[data])
# db.commit()

# 提取二进制文件
sql = "select image from cls where id=1;"
cur.execute(sql)
data = cur.fetchone() # (image,)
with open("葫芦娃.jpg",'wb') as f:
    f.write(data[0])



# 关闭游标和数据库链接
cur.close()
db.close()