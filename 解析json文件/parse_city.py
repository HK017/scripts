import json

import pymysql

file_path = r'C:\Users\yhouse\Desktop\city\城市.txt'

host_infos = []
db = pymysql.connect(host='10.10.206.32', port=3306, user='rigdev', db='dd_data_yhouse',
                     password='rJ2gWooHqz2B9E@U4KYKJtQ7gB8AfP')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

with open(file_path, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    for city_dict in load_dict:
        citys = city_dict['list']  # 城市
        for citys_dict in citys:
            city = citys_dict['list']
            for k in city:
                city_name = k['name']
                city_id = k['id']
                host_infos.append((city_id, city_name))
#
# sql = 'replace into dd_b83_app_city(city_id,city_name) values(%s,%s)'
# # 使用 execute()  方法执行 SQL 查询

cursor.executemany(query=sql, args=host_infos)
db.commit()

# # 关闭数据库连接
db.close()
