# -*- coding: UTF-8 -*- 
import pymysql.cursors


# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='proxypool', charset='utf8', cursorclass=pymysql.cursors.DictCursor)


# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据查询
#sql = "SELECT `id`, `password` FROM `users` WHERE `email`='huzhiheng@itest.info'"
#cursor.execute(sql)

##查询数据库单条数据
#result = cursor.fetchone()
#print(result)

#print("-----------华丽分割线------------")

# 执行数据查询
sql = "SELECT * FROM `proxypool`"
cursor.execute(sql)

#查询数据库多条数据
result = cursor.fetchall()
ip_get = []
for data in result:
    ip_get.append((data['ip']+":"+data['ip_port']))

for ip in ip_get:
    print(ip)
# 关闭数据连接
connection.close()