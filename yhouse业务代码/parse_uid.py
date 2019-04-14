# coding=utf-8
import re
import base64
import pymysql

# 用python2执行，因python3去掉了long函数
def decode_user_id(uid_str):
    row_str = ""
    for c in uid_str:
        c = ord(c)
        if ord("a") <= c <= ord("m"):
            c += 13
        elif ord("A") <= c <= ord("M"):
            c += 13
        elif ord("n") <= c <= ord("z"):
            c -= 13
        elif ord("N") <= c <= ord("Z"):
            c -= 13
        row_str = row_str + chr(c)
    row_str = row_str.replace("-_", "+/")
    n = len(row_str) % 4
    if n > 0:
        row_str = row_str + ("=" * n)

    uid = base64.b64decode(row_str)
    uid = re.sub('[^0-9]', '', uid)
    return (long(uid) - 462) / 357


conn = pymysql.connect(host='10.10.206.32', user='rigdev', passwd='rJ2gWooHqz2B9E@U4KYKJtQ7gB8AfP', port=3306, db='tmp_data_yhouse', charset='utf8')
sql = '''select distinct name from school5 limit 10;'''
with conn.cursor() as cur:
    cur.execute(sql)
    res = cur.fetchall()
# res的值
"""(('m.yhouse.com/m/ypass-happy/?pos=120.67004,31.284264&coordType=1',),
 ('m.yhouse.com/m/ypass-happy/?pos=120.649861,31.187228&cityId=33',),
 ('m.yhouse.com/m/ypass-happy/?pos=121.383338,31.314123&coordType=1',),
 ('m.yhouse.com/m/ypass-happy/?pos=118.107995,24.517109&cityId=100',),
 ('m.yhouse.com/m/ypass-happy/',),
 ('m.yhouse.com/m/ypass-happy/?pos=125.304355,43.869237&cityId=187',),
 ('m.yhouse.com/m/ypass-happy/?pos=120.158008,30.324837&coordType=1',),
 ('m.yhouse.com/m/ypass-happy/?cityId=70',),
 ('m.yhouse.com/m/ypass-happy/?pos=118.787309,32.066828&coordType=1',),
 ('m.yhouse.com/m/ypass-happy/?pos=114.315038,30.40383&coordType=1',))"""


uids = [(str(decode_user_id(r[0])), r[0]) for r in res]  # 取第一个是因为元组中嵌套元组


sql = """update school5 set parent_user_info_id=%s where jm_id=%s"""
with conn.cursor() as cur:
    cur.executemany(sql, args=uids)

conn.commit()
conn.close()