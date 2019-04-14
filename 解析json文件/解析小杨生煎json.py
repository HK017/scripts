import json
import pymysql
import os

os.chdir(r'C:\Users\yhouse\Desktop')
file_path = 'city.json'

host_infos = []
db = pymysql.connect(host='10.10.209.30', port=3306, user='houkai_test', db='experimental',password='zjrqbm4dVG33Mb7oPFdSnTBG4yWD9g')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

with open(file_path, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    for city_dict in load_dict:
        province = city_dict['name']   # 省
        citys = city_dict['cities']               # 城市
        for citys_dict in citys:
            city = citys_dict['name']
            counties = citys_dict['counties']
            for k in counties:
                circles = k['circles']
                area = k['name']
                for circle in circles:
                    business_area = circle['name']
                    host_infos.append((province,city,area, business_area))
        print(province, '解析完毕')


sql = 'insert into city_circles_test(province, city, area, business_area) values(%s,%s,%s,%s)'
# 使用 execute()  方法执行 SQL 查询

cursor.executemany(query=sql, args=host_infos)
db.commit()

# 关闭数据库连接
db.close()