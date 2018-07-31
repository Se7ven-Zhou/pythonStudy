# coding:utf-8

import pymysql

# 连接数据库
db_ip = "119.23.132.26"
db_port = 3306
db_name = "veehui_education"
db_user = "root"
db_pwd = "huShi!2#"

try:
    conn = pymysql.Connect(db_ip,db_user,db_pwd,db_name,db_port,charset="utf8mb4",
                           cursorclass=pymysql.cursors.DictCursor)
    # cursorclass = pymysql.cursors.DictCursor 指定返回数据为字典形式
except:
    conn.close()

# 创建游标
cousor = conn.cursor()

# 查询语句
select_sql = "select id,nickname from edu_user WHERE id in (206660,206667)"
rows = cousor.execute(select_sql) # 影响的多少行
# fetchone() 一条数据用它
# fetchall() 多条数据用它
result = cousor.fetchall()
print(result)


# 添加一条数据
add_sql = "insert into edu_user xxx VALUE('xxx','xxx')"
try:
    row = cousor.execute(add_sql)
    conn.commit()
except:
    conn.rollback() # 如果失败，事务回滚

conn.close()

"""
列表，元祖：%s 代替
字典： %(name)s 代替
data = [11,"Beckham"]
insert_sql = "insert into test(id,nickname) VALUES (%s,%s)"
#字典
data = {"id":14,"nickname":"xiaojian"}
insert_sql = "insert into test(id,nickname) VALUES (%(id)s,%(nickname)s)"

cousor.execute(insert_sql,data)
"""