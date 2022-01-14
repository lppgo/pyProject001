#!/usr/bin/env python

""" python  mysql

1: 安装mysql 驱动包  : pip install mysql-connector-python


2: 注意: mysql5.x [mysql_native_password] 和mysql8 [caching_sha2_password]  的密码加密方式发生了变化。

如果SQL语句带有参数，那么需要把参数按照位置传递给cursor.execute()方法，MySQL的占位符是%s
"""

import mysql.connector

conn = mysql.connector.connect(
    user="root", password="admin", host="localhost", database="mydb"
)

cursor = conn.cursor()

cursor.execute("insert into user(id,name,age)values(null,'python', 20)")
print(cursor.rowcount)
conn.commit()
# cursor.execute("select * from user order by id desc limit 3")
cursor.execute(
    "select * from user where name=%s and age=%s limit %s", ["python", 20, 1]
)
print(cursor.fetchall())
cursor.close()
conn.close
