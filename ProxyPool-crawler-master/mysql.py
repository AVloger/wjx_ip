# -*- coding: UTF-8 -*- 
import pymysql.cursors


# ����MySQL���ݿ�
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='proxypool', charset='utf8', cursorclass=pymysql.cursors.DictCursor)


# ͨ��cursor�����α�
cursor = connection.cursor()

# ִ�����ݲ�ѯ
#sql = "SELECT `id`, `password` FROM `users` WHERE `email`='huzhiheng@itest.info'"
#cursor.execute(sql)

##��ѯ���ݿⵥ������
#result = cursor.fetchone()
#print(result)

#print("-----------�����ָ���------------")

# ִ�����ݲ�ѯ
sql = "SELECT * FROM `proxypool`"
cursor.execute(sql)

#��ѯ���ݿ��������
result = cursor.fetchall()
ip_get = []
for data in result:
    ip_get.append((data['ip']+":"+data['ip_port']))

for ip in ip_get:
    print(ip)
# �ر���������
connection.close()